from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny] # IsAuthenticated

    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
