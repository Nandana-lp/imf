# Generated by Django 5.1.4 on 2025-03-07 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0033_alter_patienttransfer_from_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='hsp_id',
        ),
    ]
