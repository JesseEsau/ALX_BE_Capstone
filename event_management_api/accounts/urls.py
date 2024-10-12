from django.urls import path
from .views import UserRegistrationAPIView
from django.contrib.auth.views import LoginView
from .views import LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', LogoutView, name="logout"),
]