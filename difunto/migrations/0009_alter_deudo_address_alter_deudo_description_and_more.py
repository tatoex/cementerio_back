# Generated by Django 4.2.16 on 2024-12-03 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tumba', '0013_historicallote_height_historicallote_rotation_and_more'),
        ('difunto', '0008_alter_deudo_options_alter_difunto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deudo',
            name='address',
            field=models.CharField(blank=True, default='Quito', max_length=100, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='deudo',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='deudo',
            name='tipo',
            field=models.CharField(choices=[('Allegado', 'Familiar cercano'), ('Familiar', 'Miembro de la familia'), ('Conocido', 'Conocido del fallecido')], default='Conocido', max_length=50, verbose_name='tipo relacion'),
        ),
        migrations.AlterField(
            model_name='difunto',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='difunto',
            name='tumba',
            field=models.ForeignKey(blank=True, default=6000, on_delete=django.db.models.deletion.DO_NOTHING, related_name='difuntoTumba', to='tumba.tumba'),
        ),
        migrations.AlterField(
            model_name='historicaldeudo',
            name='address',
            field=models.CharField(blank=True, default='Quito', max_length=100, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='historicaldeudo',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='historicaldeudo',
            name='tipo',
            field=models.CharField(choices=[('Allegado', 'Familiar cercano'), ('Familiar', 'Miembro de la familia'), ('Conocido', 'Conocido del fallecido')], default='Conocido', max_length=50, verbose_name='tipo relacion'),
        ),
        migrations.AlterField(
            model_name='historicaldifunto',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=300, verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='historicaldifunto',
            name='tumba',
            field=models.ForeignKey(blank=True, db_constraint=False, default=6000, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tumba.tumba'),
        ),
    ]
