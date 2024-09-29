from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics

from .models import Event
from .serializers import EventSerializer

#Create Events
class EventCreateAPIView(generics.CreateAPIView):
    """Create an event"""
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

#List all future Events
class EventListAPIView(generics.ListAPIView):
    """Upcoming Events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    #Show only future events
    def get_queryset(self):
        return Event.objects.filter(date_and_time__gte=timezone.now())
    
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)




