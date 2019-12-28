from django.urls import path
from .views import ArtPageCreateView, ArtPageDetailView, ArtPageListView, ArtPageDeleteView, ArtPageUpdateView, index


# app_name = 'artists'
urlpatterns = [
    path('list-All/', ArtPageListView.as_view(), name='art-list-page'),
    path('', index, name='index'),
    path('create/', ArtPageCreateView.as_view(), name='art-create-page'),
    path('artists/<str:artist>/<str:slug>/', ArtPageDetailView.as_view(), name='art-details-page'),
    path('artists/<str:artist>/<str:slug>/delete', ArtPageDeleteView.as_view(), name='art-delete'),
    path('artists/<str:artist>/<str:slug>/update', ArtPageUpdateView.as_view(), name='art-update')
    # path('<str:artist>/', ArtistArtListView.as_view(), name='artist-list-page')
]
