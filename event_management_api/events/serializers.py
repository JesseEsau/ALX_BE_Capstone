from rest_framework import serializers
from django.utils import timezone
from .models import Event, EventRegistration
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = TagListSerializerField()
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_and_time', 'location', 'capacity', 'category']
        read_only_fields = ['organizer']


    def validate_date_and_time(self, value):
            if value < timezone.now():
                raise serializers.ValidationError({"error":"Event date cannot be in the past."})
            return value

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'
        read_only_fields = ['user', 'event']



