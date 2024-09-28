from django.urls import path
from .views import EventCreateAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('events/create/', EventCreateAPIView.as_view(), name="create_event"),
]
