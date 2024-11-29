# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.serializers.register_serializer import SignupSerializer


class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Crée l'utilisateur et le profil
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
