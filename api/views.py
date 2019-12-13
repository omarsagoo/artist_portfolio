from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from artists.models import ArtPage
from api.serializers import ArtPageSerializer
# Create your views here.
class ArtPageList(ListCreateAPIView):
    queryset = ArtPage.objects.all()
    serializer_class = ArtPageSerializer

class ArtPageDetail(RetrieveDestroyAPIView):
    queryset = ArtPage.objects.all()
    serializer_class = ArtPageSerializer