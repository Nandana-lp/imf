<<<<<<< HEAD
# Generated by Django 5.1.4 on 2025-02-08 05:03
=======
# Generated by Django 5.1.4 on 2025-02-07 06:55
>>>>>>> 07f7c58de2c66ec8f021c0e29443e31880e0a111

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0011_alter_appointment_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
<<<<<<< HEAD
            field=models.DateTimeField(),
=======
            field=models.DateField(max_length=10),
>>>>>>> 07f7c58de2c66ec8f021c0e29443e31880e0a111
        ),
    ]
