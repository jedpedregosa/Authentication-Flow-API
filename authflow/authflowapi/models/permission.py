from django.db import models

class PermissionModel(models.Model):
    class Meta:
        verbose_name = 'Permission'
    
    name = models.CharField('Name', max_length=255, unique=True)