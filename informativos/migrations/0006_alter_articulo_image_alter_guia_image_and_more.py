# Generated by Django 4.2.16 on 2024-10-24 01:07

from django.db import migrations, models
import informativos.base


class Migration(migrations.Migration):

    dependencies = [
        ('informativos', '0005_alter_historicalseccionarticulo_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='info/', validators=[informativos.base.validar_tamano_imagen], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='guia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='info/', validators=[informativos.base.validar_tamano_imagen], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='historicalarticulo',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[informativos.base.validar_tamano_imagen], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='historicalguia',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[informativos.base.validar_tamano_imagen], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='historicalservicioinfo',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[informativos.base.validar_tamano_imagen], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='servicioinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='info/', validators=[informativos.base.validar_tamano_imagen], verbose_name='Imagen'),
        ),
    ]
