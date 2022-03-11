from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Client, Product, Ombor
from .serializers import ClientSerializer, OmborSerializer, ProductSerializer


class ClientAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRUD(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRUD(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OmborAPIView(ListCreateAPIView):
    serializer_class = OmborSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ombors = Ombor.objects.filter(user=self.request.user)
        return ombors

class OmborRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = OmborSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ombors = Ombor.objects.filter(user=self.request.user)
        return ombors

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer
