from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UserRegistrationSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    """Takes user credentials and stores them in the database."""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer