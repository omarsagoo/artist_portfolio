from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# from accounts.models import CustomUser


# Create your models here.
class ArtPage(models.Model):
    title = models.CharField(max_length=150, unique=True, help_text="The title of your Artwork")

    artist = models.ForeignKey(User, on_delete=models.PROTECT, 
                               help_text="The Artist who posted this")

    slug = models.CharField(max_length=150, blank=True, editable=False,
                            help_text="Unique URL path to access this page. Generated by the system.")

    image = models.ImageField(upload_to="gallery")

    short_desc = models.CharField(max_length=1000,
                                help_text="A short description to display on the main page.")

    content = models.TextField()

    published = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page. borrowed from makewiki """
        path_components = {'slug': self.slug}
        return reverse('art-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. borrowed from makewiki """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(ArtPage, self).save(*args, **kwargs)

class Artist(User):
    pass