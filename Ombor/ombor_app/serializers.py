from rest_framework.serializers import ModelSerializer
from .models import Client,Product,Ombor


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OmborSerializer(ModelSerializer):
    class Meta:
        model = Ombor
        fields = '__all__'