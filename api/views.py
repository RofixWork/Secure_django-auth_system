from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models as api_models
from . import serializes as api_serializers


# Create your views here.
class MyTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = api_serializers.MyTokenObtainPairSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = api_serializers.UserRegisterSerializer
    queryset = api_models.User.objects.all()
    permission_classes = [AllowAny]


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": f"Hi {request.user.username}"},
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        return Response(
            {"message": f"Hi {request.user.username}, your text is {text}"},
            status=status.HTTP_200_OK,
        )
