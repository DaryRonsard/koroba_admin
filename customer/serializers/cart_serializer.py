from customer.models.cart_model import CartModel
from rest_framework import serializers

from customer.serializers.cartItem_serializer import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True) 
    total_quantity = serializers.ReadOnlyField() 
    total_price = serializers.ReadOnlyField()  

    class Meta:
        model = CartModel  
        fields = ['id', 'items', 'total_quantity', 'total_price']

