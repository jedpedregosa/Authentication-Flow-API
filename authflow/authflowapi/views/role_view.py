from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import *

class RoleApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create a Role with the given data
        '''
        serializer = RoleSerializer(data={
            'name': request.data.get('name'), 
        })
        if not serializer.is_valid():
            return Response(serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        '''
        Fetch all roles
        '''
        serializer = RoleSerializer(RoleModel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoleIdApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Fetch Specific Role From Id
        '''
        role_id = kwargs['id'] if 'id' in kwargs else False

        role = False
        if role_id: 
            role = RoleModel.objects.filter(pk=role_id).first()
        if role:
            serializer = RoleSerializer(role)
            return Response(serializer.data, 
                status=status.HTTP_200_OK)

        return Response({'role_id': 'No role found.'}, 
            status=status.HTTP_400_BAD_REQUEST)


class RolePermissionApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Assign a permission to a role
        '''
        role_id = kwargs['id'] if 'id' in kwargs else False
        permission_id = request.data.get('permission_id')
        serializer = RolePermissionFormSerializer(data={
            'permission_id': permission_id, 
            'role_id': role_id
        })
        if not serializer.is_valid():
            return Response(serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST)
        
        role = RoleModel.objects.filter(pk=role_id).first()
        if not role:
            return Response({'role_id': 'No role found.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        permission = PermissionModel.objects.filter(pk=permission_id).first()
        if not permission:
            return Response({'permission_id': 'No permission found.'}, 
                status=status.HTTP_400_BAD_REQUEST)
                
        role.permission = permission
        role.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        '''
        Fetch Permission of a Role
        '''
        role_id = kwargs['id'] if 'id' in kwargs else False
        role = False
        if role_id: 
            role = RoleModel.objects.filter(pk=role_id).first()
        if role:
            serializer = PermissionSerializer(role.permission)
            return Response(serializer.data if role.permission else None, 
                status=status.HTTP_200_OK)

        return Response({'role_id': 'No role found.'}, 
            status=status.HTTP_400_BAD_REQUEST)