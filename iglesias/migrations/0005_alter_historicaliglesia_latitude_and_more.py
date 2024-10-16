# Generated by Django 4.2.16 on 2024-10-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iglesias', '0004_remove_historicaliglesia_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaliglesia',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='latitud'),
        ),
        migrations.AlterField(
            model_name='historicaliglesia',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='longitud'),
        ),
        migrations.AlterField(
            model_name='iglesia',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='latitud'),
        ),
        migrations.AlterField(
            model_name='iglesia',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='longitud'),
        ),
    ]
