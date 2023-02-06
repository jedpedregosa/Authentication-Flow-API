from django import forms
from .common import CommonForm

class PermissionForm(CommonForm):
    name = forms.CharField(label='Permission Name', max_length=255)