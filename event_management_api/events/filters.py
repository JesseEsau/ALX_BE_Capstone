from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains', label='Search by Category')
    title = filters.CharFilter(field_name="title", lookup_expr='icontains', label='Search by Title')
    location = filters.CharFilter(field_name="location", lookup_expr='icontains', label='Event Location')


    class Meta:
        model = Event
        fields = ['title', 'location', 'category']