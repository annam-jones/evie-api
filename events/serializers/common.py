from rest_framework import serializers 
from ..models import Event

class EventSerializer(serializers.ModelSerializer):
    eventImage = serializers.URLField(source='event_image', required=False)
    
    class Meta: 
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'category', 
                 'capacity', 'organizer', 'created_by', 'attendees', 'eventImage']