# Generated by Django 4.2.16 on 2024-10-16 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iglesias', '0005_alter_historicaliglesia_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallinkredsocial',
            name='iglesia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='iglesias.iglesia'),
        ),
        migrations.AddField(
            model_name='historicallinkredsocial',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL de la red social'),
        ),
        migrations.AddField(
            model_name='linkredsocial',
            name='iglesia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redes_sociales', to='iglesias.iglesia'),
        ),
        migrations.AddField(
            model_name='linkredsocial',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL de la red social'),
        ),
        migrations.AlterField(
            model_name='historicallinkredsocial',
            name='stage_type',
            field=models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Youtube', 'Youtube')], max_length=50, verbose_name='Plataforma'),
        ),
        migrations.AlterField(
            model_name='linkredsocial',
            name='stage_type',
            field=models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Youtube', 'Youtube')], max_length=50, verbose_name='Plataforma'),
        ),
    ]
