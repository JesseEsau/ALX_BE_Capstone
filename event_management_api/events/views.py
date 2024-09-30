from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Event
from .serializers import EventSerializer
from .permissions import IsOwnerOrReadOnly

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
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    
    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


