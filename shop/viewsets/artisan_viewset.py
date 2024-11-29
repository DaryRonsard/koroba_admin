from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from base.permissions.customer_permission import IsCustomer
from shop.models.artisan_model import ArtisanModel
from shop.serializers.artisan_serializer import ArtisanSerializer

class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = ArtisanModel.objects.all()
    serializer_class = ArtisanSerializer
    permission_classes = [IsCustomer]

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password', None) 
        artisan = serializer.save() 
        if password:
            artisan.set_password(password)  
            artisan.save()

    def perform_update(self, serializer):
        """Surcharge de la méthode update pour gérer la mise à jour du mot de passe"""
        password = serializer.validated_data.pop('password', None)
        artisan = serializer.save() 
        if password:
            artisan.set_password(password) 
            artisan.save()
    
    @action(detail=False, methods=['get'], url_path='by-job/(?P<job>[^/.]+)')
    def filter_by_job(self, request, job=None):
        artisans = ArtisanModel.objects.filter(job=job)
        serializer = ArtisanSerializer(artisans, many=True)
        return Response(serializer.data)
