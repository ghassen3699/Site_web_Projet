# Generated by Django 3.2.5 on 2021-08-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrant_irregulier', '0009_remove_migrantirregulier_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='migrantirregulier',
            name='numero_cin',
            field=models.CharField(blank=True, max_length=8, unique=True, verbose_name='le numero cin'),
        ),
        migrations.AlterField(
            model_name='migrantirregulier',
            name='numero_passport',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='le numero de passport'),
        ),
    ]