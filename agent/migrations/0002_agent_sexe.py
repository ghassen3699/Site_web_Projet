# Generated by Django 3.1.7 on 2021-07-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='sexe',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='', max_length=30),
            preserve_default=False,
        ),
    ]