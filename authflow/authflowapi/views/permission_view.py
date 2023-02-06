from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import *

class PermissionApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create a Permission with the given data
        '''
        serializer = PermissionSerializer(data={
            'name': request.data.get('name'), 
        })
        if not serializer.is_valid():
            return Response(serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        '''
        Fetch all permissions
        '''
        serializer = PermissionSerializer(PermissionModel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)