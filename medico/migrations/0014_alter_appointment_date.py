# Generated by Django 5.1.4 on 2025-02-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0013_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=15),
        ),
    ]
