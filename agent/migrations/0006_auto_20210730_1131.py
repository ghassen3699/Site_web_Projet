# Generated by Django 3.1.7 on 2021-07-30 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lieu_de_travail', '0003_auto_20210729_1248'),
        ('grade_de_travail', '0003_auto_20210729_1248'),
        ('agent', '0005_auto_20210729_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='grade_de_travail_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade_de_travail.gradedetravail'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='lieu_de_travail_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lieu_de_travail.lieu_de_travail'),
        ),
    ]