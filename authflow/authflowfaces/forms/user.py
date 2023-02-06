from django import forms
from .common import CommonForm

class UserLoginForm(CommonForm):
    email = forms.EmailField(label='Email', max_length=255, required=False)
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=255)

class UserSignUpForm(UserLoginForm):
    email = forms.EmailField(label='Email', max_length=255)
