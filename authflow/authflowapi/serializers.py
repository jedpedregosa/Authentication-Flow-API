from rest_framework import serializers
from .models import *

""" Model Related Serializers """
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "password", "email", "salt"]

# Permission Serializer
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionModel
        fields = ["id", "name"]

# Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = ["id", "name", "permission"]

""" User Form Related Serializers """
# User Form Serializer
class UserFormSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=12)

# User Login Form Serializer
class UserLoginSerializer(UserFormSerializer):
    email = serializers.EmailField(max_length=255, 
        required=False, allow_blank=True, allow_null=True)
    username = serializers.CharField(max_length=30,
        required=False, allow_blank=True, allow_null=True)

""" User-Role Form Related Serializers """
# User Role Form Serializer
class UserRoleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

""" Role-Permission Form Related Serializers """
# User Login Form Serializer
class RolePermissionFormSerializer(serializers.Serializer):
    permission_id = serializers.CharField(max_length=255)
    role_id = serializers.CharField(max_length=255)