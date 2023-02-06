from rest_framework import serializers
from .forms import *

# User Serializer
class UserSignUpResultSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

# User Login Serializer
class UserLoginResultSerializer(UserSignUpResultSerializer):
    response = serializers.CharField(max_length=255)

# User Permission List Serializer
class PermissionListSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)

# Permission Serializer
class PermissionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

# Role List Serializer
class RoleListSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)

# Role Serializer
class RoleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)