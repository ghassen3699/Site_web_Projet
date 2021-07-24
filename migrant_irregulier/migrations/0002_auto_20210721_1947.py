# Generated by Django 3.1.7 on 2021-07-21 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migrant_irregulier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='migrantirregulier',
            name='sexe',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='migrantirregulier',
            name='nationalite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migrant_irregulier.nationalite'),
        ),
    ]