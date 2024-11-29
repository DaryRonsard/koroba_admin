# serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import UserModel
from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Authentification de l'utilisateur
        user = authenticate(**data)
        if not user:
            raise ValidationError("Invalid credentials")
        
        if not user.is_active:
            raise ValidationError("This account is inactive.")

        # Générer les tokens JWT pour l'utilisateur
        refresh = RefreshToken.for_user(user)
        
        # Sérialiser l'utilisateur
        user_data = {
            'id': user.id,
            'username': user.username,
            'user_type': user.user_type,
        }

        # Retourner les tokens et l'utilisateur
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_data
        }
