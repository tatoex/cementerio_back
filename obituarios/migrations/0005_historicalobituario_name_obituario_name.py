# Generated by Django 4.2.16 on 2024-10-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obituarios', '0004_alter_historicalmemoria_image_alter_memoria_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalobituario',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='homenajeado'),
        ),
        migrations.AddField(
            model_name='obituario',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='homenajeado'),
        ),
    ]