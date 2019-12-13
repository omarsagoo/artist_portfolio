from django.urls import path

from api.views import ArtPageList, ArtPageDetail

urlpatterns = [
    path('artist/', ArtPageList.as_view(), name='art_list'),
    path('artist/<int:pk>', ArtPageDetail.as_view(), name='art_detail')
]