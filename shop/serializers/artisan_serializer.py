from rest_framework import serializers
from shop.models.artisan_model import ArtisanModel

class ArtisanSerializer(serializers.ModelSerializer):
    picture_url = serializers.ReadOnlyField()
    class Meta:
        model = ArtisanModel
        fields = ['id', 'username', 'password','phone_number', 'whatsapp_number', 
                  'job_artisan', 'sex_artisan', 'picture_artisan', 'picture_url']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        validated_data['user_type'] = 'artisan'
        password = validated_data.pop('password', None)
        artisan = super().create(validated_data)
        if password:
            artisan.set_password(password)
            artisan.save()
        return artisan

    def update(self, instance, validated_data):
        validated_data['user_type'] = 'artisan'
        password = validated_data.pop('password', None)
        artisan = super().update(instance, validated_data)
        if password:
            artisan.set_password(password)
            artisan.save()
        return artisan
