# Generated by Django 4.2.16 on 2024-12-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tumba', '0021_alter_historicallote_trans_r_x_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallote',
            name='blockName',
            field=models.PositiveIntegerField(verbose_name='Lote'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='columnas',
            field=models.PositiveIntegerField(verbose_name='Numero de columnas'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='filas',
            field=models.PositiveIntegerField(verbose_name='Numero de filas'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='limite',
            field=models.PositiveIntegerField(verbose_name='Limite de espacio'),
        ),
        migrations.AlterField(
            model_name='historicallote',
            name='numbersblock',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='numero de tipo'),
        ),
        migrations.AlterField(
            model_name='historicaltumba',
            name='nicheNumber',
            field=models.PositiveIntegerField(verbose_name='tumba'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='blockName',
            field=models.PositiveIntegerField(verbose_name='Lote'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='columnas',
            field=models.PositiveIntegerField(verbose_name='Numero de columnas'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='filas',
            field=models.PositiveIntegerField(verbose_name='Numero de filas'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='limite',
            field=models.PositiveIntegerField(verbose_name='Limite de espacio'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='numbersblock',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='numero de tipo'),
        ),
        migrations.AlterField(
            model_name='tumba',
            name='nicheNumber',
            field=models.PositiveIntegerField(verbose_name='tumba'),
        ),
        migrations.AddConstraint(
            model_name='tumba',
            constraint=models.UniqueConstraint(fields=('nicheNumber', 'nameLote'), name='unique_niche_per_lote'),
        ),
    ]
