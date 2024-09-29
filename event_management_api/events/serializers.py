from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['organizer']

    title = serializers.CharField(required=True)
    date_and_time = serializers.DateTimeField(required=True)
    location = serializers.CharField(required=True)

    description = serializers.CharField(required=False)
    capacity = serializers.IntegerField(required=False)

    def validate_date_and_time(self, value):
            if value < timezone.now():
                raise serializers.ValidationError({"error":"Event date cannot be in the past."})
            return value



