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

class ArtDeleteTest(TestCase):
    def test_create_page(self):
        user = User.objects.create()

        art_page = ArtPage(artist=user, title='my art page', image=None)

        art_page.save()

        art_pages = ArtPage.objects.all()
        self.assertEqual(len(art_pages), 1)

    def test_delete_page(self):
        user = User.objects.create()

        art_page = ArtPage(artist=user, title='my art page', image=None)

        art_page.save()
        art_pages = ArtPage.objects.all()
        self.assertEqual(len(art_pages), 1)

        art_page.delete()
        art_pages = ArtPage.objects.all()
        self.assertEqual(len(art_pages), 0)

class UpdateViewTest(TestCase):
    def test_update_page(self):
        user = User.objects.create()

        art_page = ArtPage(artist=user, title='my art page', image=None)

        art_page.save()
        art_page.title = "test page"
        self.assertEqual(art_page.title, "test page")