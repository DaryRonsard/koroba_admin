from shop.models.product_model import ProductModel
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['artisan', 'product_name', 'product_description','product_price', 'product_picture']
