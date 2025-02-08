
# Generated by Django 5.1.4 on 2025-02-02 05:48

# Generated by Django 5.1.4 on 2025-02-02 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0007_patient_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('time', models.TimeField()),
                ('current_date', models.DateField(auto_now_add=True)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_id', to='medico.login')),
                ('patient_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paitent_id', to='medico.login')),
            ],
        ),
    ]
