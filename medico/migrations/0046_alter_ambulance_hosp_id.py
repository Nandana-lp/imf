# Generated by Django 5.1.4 on 2025-03-09 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0045_rename_ambulance_cat_ambulance_ambulance_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='hosp_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosp_id', to='medico.hospital'),
        ),
    ]
