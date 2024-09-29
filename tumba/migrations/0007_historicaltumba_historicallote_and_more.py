# Generated by Django 4.2.16 on 2024-09-28 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tumba', '0006_remove_disponibletumba_modified_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTumba',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('loadDate', models.DateTimeField(blank=True, editable=False, verbose_name='creacion')),
                ('updateDate', models.DateTimeField(blank=True, editable=False, verbose_name='actualizacion')),
                ('decription', models.TextField(blank=True, max_length=300, null=True, verbose_name='observaciones')),
                ('nicheNumber', models.IntegerField(verbose_name='tumba')),
                ('nicheType', models.CharField(choices=[('T', 'Tumba de tierra'), ('E', 'Tumba extramuros')], max_length=1, verbose_name='tipo')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('nameLote', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tumba.lote')),
            ],
            options={
                'verbose_name': 'historical tumba',
                'verbose_name_plural': 'historical tumbas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLote',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('loadDate', models.DateTimeField(blank=True, editable=False, verbose_name='creacion')),
                ('updateDate', models.DateTimeField(blank=True, editable=False, verbose_name='actualizacion')),
                ('decription', models.TextField(blank=True, max_length=300, null=True, verbose_name='observaciones')),
                ('blockName', models.IntegerField(verbose_name='bloque')),
                ('clasificacion', models.CharField(max_length=50, verbose_name='Tipo')),
                ('filas', models.IntegerField(verbose_name='Nuero de filas')),
                ('columnas', models.IntegerField(verbose_name='Nuero de columnas')),
                ('limite', models.IntegerField(verbose_name='Limite de espacio')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical lote',
                'verbose_name_plural': 'historical lotes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDisponibleTumba',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('loadDate', models.DateTimeField(blank=True, editable=False, verbose_name='creacion')),
                ('updateDate', models.DateTimeField(blank=True, editable=False, verbose_name='actualizacion')),
                ('decription', models.TextField(blank=True, max_length=300, null=True, verbose_name='observaciones')),
                ('startDate', models.DateTimeField(verbose_name='inicio')),
                ('endDate', models.DateTimeField(verbose_name='vence')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('numberTumba', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tumba.tumba')),
            ],
            options={
                'verbose_name': 'historical disponible tumba',
                'verbose_name_plural': 'historical disponible tumbas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
