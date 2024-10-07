from django.contrib.auth.models import User
from .models import Event
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class EventTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    #test create an Event
    def test_create_event(self):
        url = reverse('create_event')
        data = {
            'title': 'Music Concert',
            'description': 'An awesome music event.',
            'location': 'Jos City',
            'date_and_time': '2024-10-11T18:00:00Z',
            'capacity': 500,
            'category': "Music"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Music Concert')

    