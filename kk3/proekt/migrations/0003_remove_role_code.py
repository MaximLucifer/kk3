# Generated by Django 5.2 on 2025-04-18 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proekt', '0002_role_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='code',
        ),
    ]
