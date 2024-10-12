from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

from .serializers import UserRegistrationSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    """Takes user credentials and stores them in the database."""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

#log out view
def LogoutView(request):
    logout(request)
    return redirect("/")