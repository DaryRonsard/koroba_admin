# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from accounts.models import UserModel
from rest_framework.exceptions import ValidationError

from customer.models.customer_model import CustomerModel
from shop.models.artisan_model import ArtisanModel


# User = get_user_model()

JOB_CHOICES = [
    ('Coiffure', 'Coiffure'),
    ('Couture', 'Couture'),
    ('Mecanique', 'Mecanique'),
    ('Bijouterie', 'Bijouterie'),
    ('Maconnerie', 'Maconnerie'),
    ('Transport', 'Transport'),
    ('Electronique', 'Electronique'),
    ('Boucherie', 'Boucherie'),
]
SEX_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class SignupSerializer(serializers.Serializer):
    

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    user_type = serializers.ChoiceField(choices=UserModel.USER_TYPES)
    phone_number = serializers.CharField()
    whatsapp_number = serializers.CharField()

    # Champs spécifiques aux artisans
    job_artisan = serializers.ChoiceField(choices=JOB_CHOICES, required=False)
    sex_artisan = serializers.ChoiceField(choices=SEX_CHOICES, required=False)
    picture_artisan = serializers.URLField(required=False)

    def validate_username(self, value):
        # Vérifier si le nom d'utilisateur existe déjà
        if UserModel.objects.filter(username=value).exists():
            raise ValidationError(f"Le nom d'utilisateur '{value}' est déjà pris.")
        return value

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        # Créer l'utilisateur
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            whatsapp_number=validated_data['whatsapp_number'],
            user_type=user_type
        )
        
        # Créer le profil spécifique en fonction du type d'utilisateur
        if user_type == 'customer':
            CustomerModel.objects.create(user=user)
        elif user_type =='artisan':
            artisan_data = {
                'job_artisan': validated_data['job_artisan'],
                'sex_artisan': validated_data['sex_artisan'],
                'picture_artisan': validated_data.get('picture_artisan', None)
            }
            ArtisanModel.objects.create(user=user, **artisan_data)

        return user
