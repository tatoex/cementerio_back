# Generated by Django 4.2.16 on 2024-10-12 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0009_ceremonia_amount_paid_ceremonia_is_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalservicio',
            name='deudo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='deudo',
        ),
    ]