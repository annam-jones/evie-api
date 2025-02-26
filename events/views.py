from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
#from django.shortcuts import get_object_or_404
from .models import Event
from users.models import User
from .serializers.common import EventSerializer
from .serializers.populated import PopulatedEventSerializer
#from users.serializers import UserSerializer
class EventListView(APIView):

    def get(self, request):
        event_queryset = Event.objects.all()
        event_serialized = EventSerializer(event_queryset, many=True)
        return Response(event_serialized.data)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)

        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=201)

        return Response(event_serializer.errors, status=422)


class EventDetailView(APIView):

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
        serialized_event = EventSerializer(event, data=request.data, partial=True)

        if serialized_event.is_valid():
            serialized_event.save()
            return Response(serialized_event.data)

        return Response(serialized_event.errors, status=422)

    def delete(self, request, event_id):
        event = self.get_object(event_id)
        event.delete()
        return Response(status=204)
    
