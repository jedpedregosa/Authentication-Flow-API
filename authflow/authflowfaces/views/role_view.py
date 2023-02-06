from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

import requests

from ..forms import RoleForm, RolePermissionForm
from ..serializers import *

class RoleView(View):
    template_name = 'roles.html'
    form_class = RoleForm()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {
            'form': form, 
            'role_list': self.fetch_list()
        })
    
    def post(self, request, *args, **kwargs):
        form = RoleForm(request.POST)
        if form.is_valid():
            response = requests.post('http://127.0.0.1:8000/api/roles',
                data=form.cleaned_data)
            if response.status_code != 201:
                serializer = RoleSerializer(data=response.json())
                for item in serializer.initial_data:
                    form.add_error(item, serializer.initial_data[item].pop())
        return render(request, self.template_name, {
            'form': form, 
            'role_list': self.fetch_list()
        }) 

    def fetch_list(self):
        response = requests.get('http://127.0.0.1:8000/api/roles')
        role_list = False
        if response.status_code == 200 and \
            response.content:
            role_list = RoleListSerializer(response.json(), many=isinstance(response.json(),list))
        return role_list.data if role_list else None

class RolePermissionView(View):
    template_name = 'roles-permission.html'
    form_class = RolePermissionForm()

    def get(self, request, *args, **kwargs):
        form = self.form_class

        role_id = kwargs['id'] if 'id' in kwargs else False
        
        #role_fetch = requests.get(f'http://127.0.0.1:8000/api/roles/{role_id}')
        #if role_fetch.content:
        #    serializers = RoleSerializer(data=role_fetch.json())

        response = requests.get(f'http://127.0.0.1:8000/api/roles/{role_id}/permissions')
        if response.status_code != 200:
            return HttpResponseNotFound("hello")
        permission = PermissionListSerializer(response.json(), many=isinstance(response.json(),list))

        return render(request, self.template_name, {
            'form': form, 
            'perm_list': self.fetch_list(),
            'perm_selected': permission.data if 
                permission else None
        })

    def fetch_list(self):
        response = requests.get('http://127.0.0.1:8000/api/permissions')
        permission_list = False
        if response.status_code == 200 and \
            response.content:
            permission_list = PermissionListSerializer(response.json(), many=isinstance(response.json(),list))
        return permission_list.data if permission_list else None
    