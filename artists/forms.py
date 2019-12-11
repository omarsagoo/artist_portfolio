from django  import forms
from .models import ArtPage


class ArtPageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = ArtPage
        fields = ('title', 'content', 'artist', 'image')

# class ArtistForm(forms.ModelForm):
#     class Meta:
