# Generated by Django 5.1.4 on 2025-02-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0020_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
