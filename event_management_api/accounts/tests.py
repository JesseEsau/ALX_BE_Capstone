from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

class UserAuthTests(APITestCase):
    def setUp(self):
        # Create a user before testing login
        self.user = User.objects.create_user(username='testuser', password='password123')
    
    #test tegister user
    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'test2',
            'password': 'test2',
            'email': 'test2@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #test login
    def test_login_user(self):
        url = reverse('token_obtain_pair')  
        user_data = {
            'username': 'testuser',  # Same username as created in setUp
            'password': 'password123'  # Same password as created in setUp
        }
        
        # Simulate login request
        response = self.client.post(url, user_data)
        
        # Check if the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  