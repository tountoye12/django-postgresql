# Generated by Django 5.1 on 2024-08-11 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('compagny', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('mobile', models.CharField(max_length=256)),
                ('photo', models.CharField(max_length=256)),
                ('groudId', models.CharField(max_length=10)),
            ],
        ),
    ]
