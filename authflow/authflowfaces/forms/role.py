from django import forms
from .common import CommonForm

class RoleForm(CommonForm):
    name = forms.CharField(label='Role Name', max_length=255)

class RolePermissionForm(CommonForm):
    id = forms.CharField(max_length=255)
    name = forms.CharField(label='Role Name', max_length=255, required=False)
    permission = forms.CharField(label='Permission', max_length=255)