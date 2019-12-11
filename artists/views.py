from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.list import ListView
# from django.contrib.auth.models import User

from .models import ArtPage


# Create your views here.
class ArtPageDetailView(DetailView):
    ''' renders a specific art page
    use makewiki as example for creating this '''
    model = ArtPage
    template_name = "page.html"

    def get(self, request, slug):
        ''' return a specific page by slug '''
        art_page = self.get_queryset().get(slug__iexact=slug)
        return render(request, self.template_name, {'page': art_page})

class ArtPageCreateView(CreateView):
    model = ArtPage
    fields = ['title', 'content', 'artist', 'image']
    template_name = "page_create.html"

class ArtPageListView(ListView):
    model = ArtPage
    template_name = "list.html"

    def get(self, request):
        '''GET a list of all the pages '''
        art_pages = self.get_queryset().all()
        return render(request, self.template_name, {'pages': art_pages})

class ArtistArtListView(ListView):
    model = ArtPage
    template_name = 'list.html'

    def get(self, request):
        art_pages = self.model.objects.get()
        return render(request, self.template_name, {'pages': art_pages})