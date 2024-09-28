from django.urls import path
from .views import EventCreateAPIView

urlpatterns = [
    path('events/create/', EventCreateAPIView.as_view(), name="create_event"),
]
