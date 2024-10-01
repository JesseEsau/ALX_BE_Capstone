from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import filters

from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer
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

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location']
    
    
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


class EventRegistrationView(generics.GenericAPIView):
    """This view allows users to register for upcoming events."""
    
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventRegistrationSerializer

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        if event.is_full():
            return Response({"detail": f"{event.title} Event is full."}, status=status.HTTP_400_BAD_REQUEST)
            
        if event.date_and_time <= timezone.now():
            return Response({"detail": f"{event.title} is a past event. You cannot register."}, status=status.HTTP_400_BAD_REQUEST)

        if EventRegistration.objects.filter(user=request.user, event=event).exists():
            return Response({"detail": "You have already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)
            
        EventRegistration.objects.create(user=request.user, event=event)
        return Response({"detail": "Successfully registered for event."}, status=status.HTTP_200_OK)
        


       