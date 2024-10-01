from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from .models import Event, EventRegistration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['organizer']

    def validate_date_and_time(self, value):
            if value < timezone.now():
                raise serializers.ValidationError({"error":"Event date cannot be in the past."})
            return value

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'
        



