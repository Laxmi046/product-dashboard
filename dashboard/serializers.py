from rest_framework import serializers
from .models import Product, Scan

class ProductSerializer(serializers.ModelSerializer):
    scan_count = serializers.IntegerField(source='scans.count', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'scan_count']

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = '__all__'
