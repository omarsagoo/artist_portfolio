from django.urls import path
from .views import ArtPageCreateView, ArtPageDetailView, ArtPageListView, ArtistArtListView


urlpatterns = [
    path('', ArtPageListView.as_view(), name='art-list-page'),
    path('create/', ArtPageCreateView.as_view(), name='art-create-page'),
    path('<str:slug>/', ArtPageDetailView.as_view(), name='art-details-page'),
]
