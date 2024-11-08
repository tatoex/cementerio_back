# Generated by Django 4.2.16 on 2024-10-03 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkRedSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description breve')),
                ('image', models.ImageField(blank=True, null=True, upload_to='iglesias/', verbose_name='Foto')),
                ('loadDate', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updateDate', models.DateTimeField(auto_now=True, verbose_name='Actualizacion')),
                ('stage_type', models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Youtube', 'Youtube')], max_length=50, verbose_name='Etapas de las ceremonias')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description breve')),
                ('image', models.ImageField(blank=True, null=True, upload_to='iglesias/', verbose_name='Foto')),
                ('loadDate', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updateDate', models.DateTimeField(auto_now=True, verbose_name='Actualizacion')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('churches_number', models.PositiveIntegerField(default=0, verbose_name='Numero de iglesias')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Iglesia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description breve')),
                ('image', models.ImageField(blank=True, null=True, upload_to='iglesias/', verbose_name='Foto')),
                ('loadDate', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updateDate', models.DateTimeField(auto_now=True, verbose_name='Actualizacion')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitud')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longitud')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('schedule', models.TextField(blank=True, null=True, verbose_name='Horario')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='Pagina de Facebook')),
                ('priest', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sacerdote')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Logo')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iglesias', to='iglesias.parroquia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalParroquia',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description breve')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Foto')),
                ('loadDate', models.DateTimeField(blank=True, editable=False, verbose_name='Creacion')),
                ('updateDate', models.DateTimeField(blank=True, editable=False, verbose_name='Actualizacion')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('churches_number', models.PositiveIntegerField(default=0, verbose_name='Numero de iglesias')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical parroquia',
                'verbose_name_plural': 'historical parroquias',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLinkRedSocial',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description breve')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Foto')),
                ('loadDate', models.DateTimeField(blank=True, editable=False, verbose_name='Creacion')),
                ('updateDate', models.DateTimeField(blank=True, editable=False, verbose_name='Actualizacion')),
                ('stage_type', models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Youtube', 'Youtube')], max_length=50, verbose_name='Etapas de las ceremonias')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical link red social',
                'verbose_name_plural': 'historical link red socials',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIglesia',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description breve')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Foto')),
                ('loadDate', models.DateTimeField(blank=True, editable=False, verbose_name='Creacion')),
                ('updateDate', models.DateTimeField(blank=True, editable=False, verbose_name='Actualizacion')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitud')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longitud')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('schedule', models.TextField(blank=True, null=True, verbose_name='Horario')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='Pagina de Facebook')),
                ('priest', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sacerdote')),
                ('logo', models.TextField(blank=True, max_length=100, null=True, verbose_name='Logo')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parish', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='iglesias.parroquia')),
            ],
            options={
                'verbose_name': 'historical iglesia',
                'verbose_name_plural': 'historical iglesias',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
