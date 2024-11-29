from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from customer.models.cart_model import CartModel
from customer.models.orderItem_model import OrderItemModel
from customer.models.order_model import OrderModel
from customer.serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        # Les clients peuvent voir leurs commandes
        if hasattr(self.request.user, 'customermodel'):
            return OrderModel.objects.filter(customer=self.request.user)
        # Les artisans peuvent voir les commandes qui contiennent leurs produits
        if hasattr(self.request.user, 'artisanmodel'):
            return OrderModel.objects.filter(items__artisan=self.request.user.artisanmodel).distinct()
        return OrderModel.objects.none()

        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request, pk=None):
        """Permet aux artisans de mettre à jour le statut d'une commande"""
        if not hasattr(request.user, 'artisanmodel'):
            return Response({"detail": "Vous n'êtes pas autorisé à effectuer cette action."}, status=status.HTTP_403_FORBIDDEN)

        order = self.get_object()
        status = request.data.get('status')
        if status not in [choice[0] for choice in OrderModel.STATUS_CHOICES]:
            return Response({"detail": "Statut invalide."}, status=status.HTTP_400_BAD_REQUEST)

        order.status = status
        order.save()
        return Response({"detail": "Statut de la commande mis à jour."})

    def perform_create(self, serializer):
        cart = CartModel.objects.get(customer=self.request.user)
        total_amount = 0
        items = []

        for item in cart.items.all():
            total_price = item.quantity * item.product.price
            total_amount += total_price

            order_item = OrderItemModel(
                product=item.product,
                artisan=item.product.artisan,
                quantity=item.quantity,
                price=item.product.price,
                total_price=total_price
            )
            items.append(order_item)

        commission_amount = total_amount * 0.05
        order = serializer.save(
            customer=self.request.user,
            total_amount=total_amount,
            commission_amount=commission_amount
        )

        for order_item in items:
            order_item.order = order
            order_item.save()

        cart.items.all().delete()