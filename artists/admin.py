from django.contrib import admin
from .models import ArtPage

# Register your models here.
class ArtPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'artist', 'image', 'created', 'modified')

admin.site.register(ArtPage)
 