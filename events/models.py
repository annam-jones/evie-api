from django.db import models
from users.models import User

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Outdoors', 'Outdoors'),
        ('Music', 'Music'),
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Community', 'Community'),
        ('Sports', 'Sports'),
        ('Food', 'Food'),
        ('Education', 'Education'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    capacity = models.IntegerField(blank=True, null=True)
    organizer = models.CharField(max_length=255)
    event_image = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events")
    attendees = models.ManyToManyField(User, related_name="attending_events", blank=True)
    
    def __str__(self):
        return self.title