from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .models import Event, EventRegistration, Comment
from .serializers import EventSerializer, EventRegistrationSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import EventFilter

#Create Events
class EventCreateAPIView(generics.CreateAPIView):
    """Accepts details required to create an event and stores it in the database if all required details are provided like Title, Location and Capacity"""
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

#List all future Events
class EventListAPIView(generics.ListAPIView):
    """List all upcoming events."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter

    #Show only future events
    def get_queryset(self):
        return Event.objects.filter(date_and_time__gte=timezone.now())

#List past Events
class PastEventListView(generics.ListAPIView):
    """List all past events"""
    serializer_class = EventSerializer

    #list only past events
    def get_queryset(self):
        return Event.objects.filter(date_and_time__lte=timezone.now())

#View, update and delete an event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Accepts GET, PUT, PATCH and DELETE methods.
    
        GET: Retrieves details of an event.

        PUT: Edit all details of an Event. 
        
        PATCH: Edit a single detail of an Event, e.g title.

        DELETE: Deletes an event from the database.
    """
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

#view to register for an event
class EventRegistrationView(generics.ListCreateAPIView):
    """Allows users to register for upcoming events and view total registrations."""

    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=self.kwargs['event_id'])

        if event.is_full():
            return Response({"detail": f"{event.title} Event is full."}, status=status.HTTP_400_BAD_REQUEST)
            
        if event.date_and_time <= timezone.now():
            return Response({"detail": f"{event.title} is a past event. You cannot register."}, status=status.HTTP_400_BAD_REQUEST)

        if EventRegistration.objects.filter(user=request.user, event=event).exists():
            return Response({"detail": "You have already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)
            
        EventRegistration.objects.create(user=request.user, event=event)
        return Response({"detail": f"successfully registered for event: {event.title}"}, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=self.kwargs['event_id'])

        total_registrations = EventRegistration.objects.filter(event=event).count()
        return Response({"detail": f"{total_registrations} registered for {event.title}"})

#comment on past event
class CommentCreateView(generics.GenericAPIView):
    """Accepts POST method and creates a comment on a past Event."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, event_pk):
        event = get_object_or_404(Event, id=event_pk)
        if event.date_and_time > timezone.now():
            return Response({"detail": "Can't give feedback on a future event."}, status=status.HTTP_400_BAD_REQUEST)
        Comment.objects.create(user=request.user, event=event)
        return Response({"detail": "Feedback submitted."}, status=status.HTTP_201_CREATED)

    
#view for retrieving, updating, and deleting a comment
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Accepts GET, PUT, PATCH and DELETE methods.
    
        GET: Retrieves details of a comment(feedback).

        PUT: Edit all details of a comment. 
        
        PATCH: Edit a single detail of a comment, e.g title.
        
        DELETE: Deletes an comment from the database.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
