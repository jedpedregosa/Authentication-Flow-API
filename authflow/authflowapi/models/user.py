from django.db import models
from . import RoleModel

class UserModel(models.Model):
    class Meta:
        verbose_name = 'User'

    username = models.CharField('Username', max_length=30, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)

    roles = models.ManyToManyField(RoleModel)