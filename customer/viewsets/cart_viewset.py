from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from customer.models.cart_model import CartModel
from customer.serializers.cart_serializer import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartModel.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @action(detail=False, methods=['get'], url_path='by-status/(?P<status>[^/.]+)')
    def filter_by_status(self, request, status=None):
        carts = CartModel.objects.filter(status=status)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            return self.queryset.filter(customer_id=customer_id)
        return self.queryset
