from django.db import models
from . import PermissionModel

class RoleModel(models.Model):
    class Meta:
        verbose_name = 'Role'
    
    name = models.CharField('Name', max_length=255, unique=True)
    permission = models.ForeignKey(PermissionModel, null=True, on_delete=models.SET_NULL)