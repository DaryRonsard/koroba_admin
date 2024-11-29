from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from shop.models.product_model import ProductModel
from shop.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name_product', 'artisan__job', 'artisan__username']  # Recherche par nom de produit, métier de l'artisan ou pseudo
    ordering_fields = ['produits_price', 'name_product']

    @action(detail=False, methods=['get'], url_path='by-user/(?P<user_id>[^/.]+)')
    def list_by_user(self, request, user_id=None):
        products = ProductModel.objects.filter(artisan_id=user_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_path='filter')
    def filter_products(self, request):
        """Filtrer les produits par différents critères."""
        queryset = self.filter_queryset(self.get_queryset())

        # Filtrage par prix (optionnel)
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
