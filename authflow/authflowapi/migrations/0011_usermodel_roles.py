# Generated by Django 4.1.5 on 2023-02-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authflowapi', '0010_rolemodel_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='roles',
            field=models.ManyToManyField(to='authflowapi.rolemodel'),
        ),
    ]
