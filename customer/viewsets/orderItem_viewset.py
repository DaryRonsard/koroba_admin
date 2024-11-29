from rest_framework import viewsets
from customer.models.orderItem_model import OrderItemModel
from customer.serializers.orderItem_serializer import OrderItemSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItemModel.objects.all()
    serializer_class = OrderItemSerializer
    # permission_classes = [IsAuthenticated]