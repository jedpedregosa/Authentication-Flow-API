# Generated by Django 4.1.5 on 2023-02-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authflowapi', '0006_alter_permissionmodel_access_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionmodel',
            name='access',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Access'),
        ),
        migrations.AlterField(
            model_name='permissionmodel',
            name='delete',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Delete'),
        ),
        migrations.AlterField(
            model_name='permissionmodel',
            name='read',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Read'),
        ),
    ]