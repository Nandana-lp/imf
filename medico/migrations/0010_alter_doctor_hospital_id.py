# Generated by Django 5.1.4 on 2025-02-07 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0009_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital_id', to='medico.hospital'),
        ),
    ]
