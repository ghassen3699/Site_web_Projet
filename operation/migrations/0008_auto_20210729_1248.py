# Generated by Django 3.1.7 on 2021-07-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_alter_operationterminer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationterminer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
