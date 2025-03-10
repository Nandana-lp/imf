# Generated by Django 5.1.4 on 2025-02-14 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0037_alter_patient_login_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='login_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='medico.login'),
        ),
    ]
