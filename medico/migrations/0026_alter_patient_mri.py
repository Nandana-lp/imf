# Generated by Django 5.1.4 on 2025-02-13 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0025_patient_mri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='MRI',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
