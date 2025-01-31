# Generated by Django 4.2.16 on 2024-12-09 22:36

from django.db import migrations, models
import django.utils.timezone
import obituarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('obituarios', '0002_alter_etapasobituario_options_alter_memoria_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalobituario',
            name='date_born',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='historicalobituario',
            name='date_dead',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='fecha de fallecimiento'),
        ),
        migrations.AddField(
            model_name='historicalobituario',
            name='image_dif',
            field=models.TextField(blank=True, default='N/A', max_length=100, validators=[obituarios.models.validar_tamano_imagen], verbose_name='Imagen opcional'),
        ),
        migrations.AddField(
            model_name='historicalobituario',
            name='name',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='homenajeado'),
        ),
        migrations.AddField(
            model_name='obituario',
            name='date_born',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='obituario',
            name='date_dead',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='fecha de fallecimiento'),
        ),
        migrations.AddField(
            model_name='obituario',
            name='image_dif',
            field=models.ImageField(blank=True, default='N/A', upload_to='obituario/', validators=[obituarios.models.validar_tamano_imagen], verbose_name='Imagen opcional'),
        ),
        migrations.AddField(
            model_name='obituario',
            name='name',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='homenajeado'),
        ),
        migrations.AlterField(
            model_name='baseobituario',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='baseobituario',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='etapasobituario',
            name='place',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='lugar de la ceremonia'),
        ),
        migrations.AlterField(
            model_name='historicaletapasobituario',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='historicaletapasobituario',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='historicaletapasobituario',
            name='place',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='lugar de la ceremonia'),
        ),
        migrations.AlterField(
            model_name='historicalmemoria',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='historicalmemoria',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='historicalmemoria',
            name='image',
            field=models.TextField(blank=True, default='N/A', max_length=100, validators=[obituarios.models.validar_tamano_imagen], verbose_name='Imagen opcional'),
        ),
        migrations.AlterField(
            model_name='historicalmemoria',
            name='relationship',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='Relacion con el difunto'),
        ),
        migrations.AlterField(
            model_name='historicalobituario',
            name='cementery',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='cemeterio'),
        ),
        migrations.AlterField(
            model_name='historicalobituario',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='historicalobituario',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='historicalobituario',
            name='obituary_detail',
            field=models.TextField(verbose_name='Detalle del obituario'),
        ),
        migrations.AlterField(
            model_name='historicalobituario',
            name='place',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='lugar de la ceremonia'),
        ),
        migrations.AlterField(
            model_name='memoria',
            name='image',
            field=models.ImageField(blank=True, default='N/A', upload_to='memories/', validators=[obituarios.models.validar_tamano_imagen], verbose_name='Imagen opcional'),
        ),
        migrations.AlterField(
            model_name='memoria',
            name='relationship',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='Relacion con el difunto'),
        ),
        migrations.AlterField(
            model_name='obituario',
            name='cementery',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='cemeterio'),
        ),
        migrations.AlterField(
            model_name='obituario',
            name='obituary_detail',
            field=models.TextField(verbose_name='Detalle del obituario'),
        ),
        migrations.AlterField(
            model_name='obituario',
            name='place',
            field=models.CharField(blank=True, default='N/A', max_length=200, verbose_name='lugar de la ceremonia'),
        ),
    ]
