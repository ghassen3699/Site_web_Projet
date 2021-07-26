# Generated by Django 3.1.7 on 2021-07-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('adresse_mail', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
    ]