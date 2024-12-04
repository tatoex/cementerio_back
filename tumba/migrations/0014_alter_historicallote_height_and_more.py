# Generated by Django 4.2.16 on 2024-12-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tumba', '0013_historicallote_height_historicallote_rotation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallote',
            name='height',
            field=models.FloatField(blank='true', default=0.1, verbose_name='alto'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='rotation',
            field=models.FloatField(blank='true', default=0.1, verbose_name='rotacion'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='text_x',
            field=models.FloatField(blank='true', default=0.1, verbose_name='text x'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='text_y',
            field=models.FloatField(blank='true', default=0.1, verbose_name='text y'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='width',
            field=models.FloatField(blank='true', default=0.1, verbose_name='ancho'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='x',
            field=models.FloatField(blank='true', default=0.1, verbose_name='x'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='y',
            field=models.FloatField(blank='true', default=0.1, verbose_name='y'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='height',
            field=models.FloatField(blank='true', default=0.1, verbose_name='alto'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='rotation',
            field=models.FloatField(blank='true', default=0.1, verbose_name='rotacion'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='text_x',
            field=models.FloatField(blank='true', default=0.1, verbose_name='text x'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='text_y',
            field=models.FloatField(blank='true', default=0.1, verbose_name='text y'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='width',
            field=models.FloatField(blank='true', default=0.1, verbose_name='ancho'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='x',
            field=models.FloatField(blank='true', default=0.1, verbose_name='x'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='y',
            field=models.FloatField(blank='true', default=0.1, verbose_name='y'),
        ),
    ]