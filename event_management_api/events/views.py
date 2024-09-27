from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ViewSet):
    """List and Retrieve Events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer

