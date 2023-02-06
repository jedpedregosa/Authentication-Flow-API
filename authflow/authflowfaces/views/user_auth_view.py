from django.shortcuts import render
from django.views import View

import requests

from ..forms import UserSignUpForm
from ..serializers import *

class UserView(View):
    template_name = 'signup.html'
    form_class = UserSignUpForm()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            response = requests.post('http://127.0.0.1:8000/api/signup',
                data=form.cleaned_data)
            if response.status_code == 201:
                form.fields['has_result'].initial = True
                form.fields['action_result'].initial = "User added succesfully."
            else:
                serializer = UserSignUpResultSerializer(data=response.json())
                for item in serializer.initial_data:
                    form.add_error(item, serializer.initial_data[item].pop())
        return render(request, self.template_name, {'form': form}) 

class UserLoginView(View):
    template_name = 'login.html'
    form_class = UserLoginForm()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            response = requests.get('http://127.0.0.1:8000/api/login',
                data=form.cleaned_data)
            serializer = UserSignUpResultSerializer(data=response.json())
            for item in serializer.initial_data:
                if item == 'email':
                    continue
                value = serializer.initial_data[item].pop()
                if response.status_code == 200:
                    form.fields['has_result'].initial = True
                    form.fields['action_result'].initial = value
                    break
                else:
                    form.add_error(item, value)        
        return render(request, self.template_name, {'form': form}) 