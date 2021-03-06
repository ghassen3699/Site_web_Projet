# Generated by Django 3.1.7 on 2021-07-18 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commissariat_De_Police',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_commissariat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_province', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lieu_De_Travail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commissariat_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lieu_de_travail.commissariat_de_police')),
                ('province_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lieu_de_travail.province')),
                ('region_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lieu_de_travail.region')),
            ],
        ),
    ]
