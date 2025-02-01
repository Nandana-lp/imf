# Generated by Django 5.1.4 on 2025-01-30 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('age', models.CharField(max_length=3)),
                ('hospital_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medico.login')),
            ],
        ),
    ]
