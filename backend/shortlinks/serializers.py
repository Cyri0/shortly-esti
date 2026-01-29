from rest_framework.serializers import ModelSerializer
from .models import ShortLink

class ShortLinkSerializer(ModelSerializer):
    class Meta:
        model = ShortLink
        fields = '__all__'
