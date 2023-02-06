from django.shortcuts import render
from django.views import View

import requests

from ..forms import PermissionForm
from ..serializers import *

class PermissionView(View):
    template_name = 'permissions.html'
    form_class = PermissionForm()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {
            'form': form, 
            'perm_list': self.fetch_list()
        })
    
    def post(self, request, *args, **kwargs):
        form = PermissionForm(request.POST)
        if form.is_valid():
            response = requests.post('http://127.0.0.1:8000/api/permissions',
                data=form.cleaned_data)
            if response.status_code != 201:
                serializer = PermissionSerializer(data=response.json())
                for item in serializer.initial_data:
                    form.add_error(item, serializer.initial_data[item].pop())
        return render(request, self.template_name, {
            'form': form, 
            'perm_list': self.fetch_list()
        }) 

    def fetch_list(self):
        response = requests.get('http://127.0.0.1:8000/api/permissions')
        permission_list = False
        if response.status_code == 200 and \
            response.content:
            permission_list = PermissionListSerializer(response.json(), many=isinstance(response.json(),list))
        return permission_list.data if permission_list else None