# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.serializers.login_serializer import LoginSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
