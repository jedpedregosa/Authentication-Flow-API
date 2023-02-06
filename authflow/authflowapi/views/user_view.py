from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import *

class UserRoleApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Add a Role to a User
        '''
        data = request.data.get('role_ids')
        user_id = kwargs['id'] if 'id' in kwargs else False

        serializer = UserRoleSerializer(data=data, many=isinstance(data, list))
        if not serializer.is_valid():
            return Response(serializer.errors, 
               status=status.HTTP_400_BAD_REQUEST)
        user = UserModel.objects.filter(pk=user_id).first()
        if not user:
            return Response({'user_id': 'No user found.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        for item in serializer.initial_data:
            role_id = item.pop('id', [])
            role = RoleModel.objects.filter(pk=role_id).first()
            if role:
                user.roles.add(role)
                user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, *args, **kwargs):
        '''
        Fetch all Roles from a User
        '''
        user_id = kwargs['id'] if 'id' in kwargs else False
        user = False
        if user_id:
            user = UserModel.objects.filter(pk=user_id).first()
        if user:
            serializer = RoleSerializer(user.roles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'user_id': 'No user found.'}, 
                status=status.HTTP_400_BAD_REQUEST)

class UserPermissionApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Fetch all Permission from a User
        '''
        user_id = kwargs['id'] if 'id' in kwargs else False
        user = False
        if user_id: 
            user = UserModel.objects.filter(pk=user_id).first()
        if not user:
            return Response({'user_id': 'No user found.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        permissions = []
        for role_id in user.roles.all():
            if role_id.permission:
                permissions.append(role_id.permission)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)