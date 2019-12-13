from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User

from artists.models import ArtPage
# Create your tests here.

class ApiResponseTest(TestCase):
    def test_api_status_code(self):
        response = self.client.get('/api/artist')
        self.assertEqual(response.status_code, 301)

    def test_specific_api_status_code(self):
        user = User()
        user.save()

        page = ArtPage(artist=user, title="test", content="test page")
        page.save()
        response = self.client.get(f'/api/artist/{page.id}')
        self.assertEqual(response.status_code, 200)