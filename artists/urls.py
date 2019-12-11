from django.urls import path
from .views import ArtPageCreateView, ArtPageDetailView, ArtPageListView


urlpatterns = [
    path('', ArtPageListView.as_view(), name='art-list-page'),
    path('create/', ArtPageCreateView.as_view(), name='art-create-page'),
    path('artists/<str:artist>/<str:slug>/', ArtPageDetailView.as_view(), name='art-details-page'),
    # path('<str:artist>/', ArtistArtListView.as_view(), name='artist-list-page')
]
