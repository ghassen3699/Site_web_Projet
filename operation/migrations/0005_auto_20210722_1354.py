# Generated by Django 3.1.7 on 2021-07-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_operationterminer_date_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationterminer',
            name='date_operation',
            field=models.DateField(verbose_name="la date de l'operation"),
        ),
    ]
