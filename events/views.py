from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Event
from users.models import User
from .serializers.common import EventSerializer
from .serializers.populated import PopulatedEventSerializer
from users.serializers.common import UserSerializer 

class EventListView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        events = Event.objects.all()
        serialized_events = EventSerializer(events, many=True)
        return Response(serialized_events.data, status=200)

    def post(self, request):
        request.data["created_by"] = request.user.id  
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=201)

        return Response(event_serializer.errors, status=400)
    
class EventDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, event_id):
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise NotFound('Event not found.')

    def get(self, request, event_id):
        event = self.get_object(event_id)
        serialized_event = PopulatedEventSerializer(event)
        return Response(serialized_event.data)

    def put(self, request, event_id):
        event = self.get_object(event_id)
        
        if event.created_by != request.user:
            return Response({"message": "You do not have permission to edit this event"}, status=403)
        
        serialized_event = EventSerializer(event, data=request.data, partial=True)

        if serialized_event.is_valid():
            serialized_event.save()
            return Response(serialized_event.data)

        return Response(serialized_event.errors, status=422)

    def delete(self, request, event_id):
        event = self.get_object(event_id)
        
        if event.created_by != request.user:
            return Response({"message": "You do not have permission to delete this event"}, status=403)
            
        event.delete()
        return Response(status=204)

class ToggleAttendanceView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        user = request.user

        if user in event.attendees.all():
            event.attendees.remove(user)  
            return Response({"message": f"You have left {event.title}"}, status=200)

        event.attendees.add(user) 
        return Response({"message": f"You are now attending {event.title}"}, status=200)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        user = request.user
        events_attending = user.attending_events.all()  
        serialized_events = EventSerializer(events_attending, many=True)

        user_data = UserSerializer(user).data
        user_data["attending_events"] = serialized_events.data  

        return Response(user_data)