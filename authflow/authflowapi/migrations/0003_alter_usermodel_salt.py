# Generated by Django 4.1.5 on 2023-01-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authflowapi', '0002_usermodel_salt_alter_usermodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='salt',
            field=models.CharField(max_length=255),
        ),
    ]