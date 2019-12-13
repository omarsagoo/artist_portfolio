from django.test import TestCase
from .models import ArtPage
from django.contrib.auth.models import User


# Create your tests here.
class ArtPageTest(TestCase):
    def test_page_slugify_on_save(self):
        # create a user to test 
        user = User()
        user.save()

        page = ArtPage(artist=user, title='my art page', image=None)
        page.save()

        self.assertEqual(page.slug, 'my-art-page')

class ArtListTest(TestCase):
    def test_multiple_pages(self):
        user = User.objects.create()

        ArtPage(artist=user, title='my art page', image=None)
        ArtPage(artist=user, title='my second art page', image=None)

        response = self.client.get('/')
        
        self.assertEqual(response.status_code, 200)

