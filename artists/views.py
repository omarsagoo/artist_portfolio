from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse
import requests 

from .forms import ArtPageForm
from .models import ArtPage



def get_api_quote():
    url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"

    headers = {
        'x-rapidapi-host': "matchilling-tronald-dump-v1.p.rapidapi.com",
        'x-rapidapi-key': "d3768e1816msh827bc58f22bcdd0p1689a1jsn8fa0a0bfe2d2",
        'accept': "application/hal+json"
        }

    response = requests.request("GET", url, headers=headers)
    quote_json = response.json()
    
    return quote_json['value']

# Create your views here.
class ArtPageDetailView(DetailView):
    ''' renders a specific art page
    use makewiki as example for creating this '''
    model = ArtPage
    template_name = "page.html"

    def get(self, request, artist, slug):
        ''' return a specific page by slug '''
        art_page = self.get_queryset().get(slug__iexact=slug)
        trump_quote = get_api_quote()
        # print(ArtPage.artist.get_username())
        return render(request, self.template_name, {'page': art_page, 'trump':trump_quote})

class ArtPageUpdateView(UpdateView):
    template_name = "page_create.html"
    form_class = ArtPageForm
    model = ArtPage
    success_url = "/"

    def get_object(self):
        ''' return a specific page by slug '''
        slug = self.kwargs.get('slug')
        return get_object_or_404(ArtPage, slug=slug)

    # def form_valid(self, form):
    #     return super().form_valid(form)


class ArtPageDeleteView(DeleteView):
    model = ArtPage
    template_name = "page_delete.html"
    # success_url = '/'

    def get_object(self):
        # art_page = self.get_queryset().get(slug__iexact=slug)
        slug = self.kwargs.get('slug')
        return get_object_or_404(ArtPage, slug=slug)

    def get_success_url(self):
        return reverse('art-list-page')


class ArtPageCreateView(CreateView):
    # model = ArtPage
    template_name = "page_create.html"
    form_class = ArtPageForm
    success_url = "/" 

    def form_valid(self, form):
        return super().form_valid(form)


class ArtPageListView(ListView):
    model = ArtPage
    template_name = "list.html"

    def get(self, request):
        '''GET a list of all the pages '''
        art_pages = self.get_queryset().all()
        return render(request, self.template_name, {'pages': art_pages})

# class ArtistArtListView(ListView):
#     model = ArtPage
#     template_name = 'list.html'

#     def get(self, request, artist):
#         art_pages = self.get_queryset().get(artist__iexact=artist)
#         return render(request, self.template_name, {'pages': art_pages})