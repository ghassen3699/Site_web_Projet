# Generated by Django 3.2.5 on 2021-08-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_de_travail', '0003_auto_20210729_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradedetravail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
