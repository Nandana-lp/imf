# Generated by Django 5.1.4 on 2025-03-09 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0042_merge_20250307_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='MRI',
            new_name='MR',
        ),
    ]
