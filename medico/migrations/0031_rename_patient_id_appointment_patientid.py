# Generated by Django 5.1.4 on 2025-02-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0030_merge_0025_merge_20250212_1459_0029_alter_patient_mri'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_id',
            new_name='patientid',
        ),
    ]
