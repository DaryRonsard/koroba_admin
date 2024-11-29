from customer.models.cartsItem_models import CartItemModel
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = ['id', 'product', 'quantity']
