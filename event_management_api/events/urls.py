from django.urls import path
from .views import EventCreateAPIView, EventListAPIView, EventDetailView, EventRegistrationView

urlpatterns = [
    path('events/create/', EventCreateAPIView.as_view(), name="create_event"),
    path('events/', EventListAPIView.as_view(), name="events_list"),
    path('events/<int:pk>/', EventDetailView.as_view(), name="event_detail"),
    path('events/<int:event_id>/register/', EventRegistrationView.as_view(), name="register_for_event"),
]
