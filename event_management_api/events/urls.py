from django.urls import path
from .views import EventCreateAPIView, EventListAPIView, EventDetailView

urlpatterns = [
    path('events/create/', EventCreateAPIView.as_view(), name="create_event"),
    path('events/', EventListAPIView.as_view(), name="events_list"),
    path('events/<int:pk>/', EventDetailView.as_view(), name="event_detail"),
]
