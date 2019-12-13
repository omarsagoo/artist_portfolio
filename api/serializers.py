from rest_framework.serializers import ModelSerializer

from artists.models import ArtPage

class ArtPageSerializer(ModelSerializer):
    class Meta:
        model = ArtPage
        fields = '__all__'

