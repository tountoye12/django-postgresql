# Generated by Django 5.1 on 2024-08-11 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Employee',
        ),
        migrations.RenameModel(
            old_name='Group',
            new_name='EmployeeGroup',
        ),
    ]
