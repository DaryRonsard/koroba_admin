from rest_framework import viewsets
from base.permissions.artisan_permission import IsArtisan
from customer.models.customer_model import CustomerModel
from customer.serializers.customer_serializer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsArtisan]
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password', None)
        customer = serializer.save()
        if password:
            customer.set_password(password)
            customer.save() 

    def perform_update(self, serializer):
        password = serializer.validated_data.pop('password', None)
        customer = serializer.save() 
        if password:
            customer.set_password(password)
            customer.save()
