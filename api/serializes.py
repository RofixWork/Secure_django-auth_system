from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["full_name"] = user.full_name
        token["email"] = user.email
        token["image"] = user.profile.image.url if user.profile else ""

        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def validate(self, attrs: dict):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password and password2 and password != password2:
            raise serializers.ValidationError(
                "Passwords must match.", status.HTTP_400_BAD_REQUEST
            )

        return super().validate(attrs)

    def create(self, validated_data: dict):
        user = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=make_password(validated_data.get("password")),
        )
        return user
