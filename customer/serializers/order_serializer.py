from rest_framework import serializers

from customer.models.order_model import OrderModel
from customer.serializers.orderItem_serializer import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderModel
        fields = ['id', 'customer', 'status', 'total_amount', 'commission_amount', 'created_at', 'items']