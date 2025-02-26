from django.urls import path
from .views import EventListView, EventDetailView, ToggleAttendanceView, UserProfileView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),  
    path('events/<int:event_id>/', EventDetailView.as_view(), name='event-detail'),  
    path('events/<int:event_id>/attend/', ToggleAttendanceView.as_view(), name='toggle-attendance'),  
    path('events/profile/', UserProfileView.as_view(), name='user-profile'),  
]
