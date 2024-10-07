from rest_framework import serializers
from django.utils import timezone

from .models import Event, EventRegistration, Comment
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = TagListSerializerField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_and_time', 'location', 'capacity', 'category', 'created_at']
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
    
    


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'user', 'event', 'created_at']

    
