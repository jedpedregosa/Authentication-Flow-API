from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

import hashlib, uuid

from ..serializers import *

to_hash = lambda _pass, salt: hashlib.sha512(
    _pass.encode('utf-8') + salt.encode('utf-8')).hexdigest()

class UserApiView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create User with the given user data
        '''
        data = {
            'username': request.data.get('username'), 
            'password': request.data.get('password'), 
            'email': request.data.get('email'),
        }

        form_serializer = UserFormSerializer(data=data)
        if not form_serializer.is_valid():
            return Response(form_serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST)
        
        # Generate a salt
        data['salt'] = uuid.uuid4().hex
        # Hash password with salt
        data['password'] = hashlib.sha512(data['password']
            .encode('utf-8') + data['salt'].encode('utf-8')).hexdigest()
        model_serializer = UserSerializer(data=data)
        
        # Check if username and email are unique on both fields
        is_taken = UserModel.objects.filter(
            Q(username=data['email']) | Q(email=data['username']))
        if not model_serializer.is_valid() or is_taken:
            return Response(model_serializer.errors or 
                {'response': 'Username or email already exists.'}, 
                status=status.HTTP_400_BAD_REQUEST)

        model_serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class UserLoginApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Authenticate the user
        '''
        data = {
            'username': request.data.get('username'), 
            'password': request.data.get('password'),
            'email': request.data.get('email')
        }
        form_serializer = UserLoginSerializer(data=data)
        if not form_serializer.is_valid():
            return Response(form_serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST)

        auth_user = UserModel.objects.filter(
            Q(email=data['email']) | Q(username=data['username'])
            | Q(email=data['username']))
        if not auth_user:
            return Response({'response': ['Username or email not found.']}, 
                status=status.HTTP_400_BAD_REQUEST)

        for user in list(auth_user):
            # Check if a hashed password matches
            if to_hash(data['password'], user.salt) == user.password:
                return Response({'response': [f'User {user.username} sucessfully logged in.']}, 
                    status=status.HTTP_200_OK)
        
        return Response({'response': ['Username or password is incorrect.']}, 
            status=status.HTTP_400_BAD_REQUEST)