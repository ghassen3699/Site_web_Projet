# Generated by Django 3.1.7 on 2021-07-22 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_operationterminer_nombre_des_migrants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationterminer',
            name='date_operation',
        ),
    ]
