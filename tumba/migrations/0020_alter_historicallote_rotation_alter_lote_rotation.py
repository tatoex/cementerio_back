# Generated by Django 4.2.16 on 2024-12-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tumba', '0019_alter_historicallote_text_x_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallote',
            name='rotation',
            field=models.IntegerField(blank='true', default=0, verbose_name='rotacion'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='rotation',
            field=models.IntegerField(blank='true', default=0, verbose_name='rotacion'),
        ),
    ]
