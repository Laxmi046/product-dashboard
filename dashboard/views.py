from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Scan
from .serializers import ProductSerializer, ScanSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ScanViewSet(viewsets.ModelViewSet):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

# Create your views here.
