# Generated by Django 4.2.16 on 2024-09-30 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('difunto', '0006_deudo_tipo_historicaldeudo_tipo'),
        ('servicio', '0005_rename_decription_ceremonia_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalservicio',
            name='deudo',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='difunto.deudo'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='deudo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='servicioDeudo', to='difunto.deudo'),
        ),
        migrations.AlterField(
            model_name='ceremonia',
            name='names',
            field=models.CharField(choices=[('Cremacion', 'Cremación'), ('Inhumacion', 'Inhumación'), ('Exhumacion', 'Exhumación'), ('Mantenimiento', 'Mantenimiento')], max_length=50, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='historicalceremonia',
            name='names',
            field=models.CharField(choices=[('Cremacion', 'Cremación'), ('Inhumacion', 'Inhumación'), ('Exhumacion', 'Exhumación'), ('Mantenimiento', 'Mantenimiento')], max_length=50, verbose_name='tipo'),
        ),
    ]
