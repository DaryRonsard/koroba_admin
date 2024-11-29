from rest_framework import viewsets
from customer.models.cartsItem_models import CartItemModel
from customer.serializers.cartItem_serializer import CartItemSerializer
from customer.models.cartsItem_models import CartItemModel
from customer.serializers.cartItem_serializer import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItemModel.objects.all()
    serializer_class = CartItemSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = CartItemModel.objects.get(customer=self.request.user)
        serializer.save(cart=cart)
