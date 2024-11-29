from rest_framework import serializers

from customer.models.orderItem_model import OrderItemModel

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = ['id', 'product', 'artisan', 'quantity', 'price', 'total_price']