from django.db import models
# Create your models here.
class Login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    user_type=models.CharField(max_length=20)
class Hospital(models.Model):
    hospital_name=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    district=models.CharField(max_length=25)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE, null=True , blank=True)
class Patient(models.Model):
    patient_name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=25)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=15)
    date_of_birth=models.CharField(max_length=15)
    contact=models.CharField(max_length=15)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE, null=True , blank=True)
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    specialization=models.CharField(max_length=25)
    gender=models.CharField(max_length=15)
    age=models.CharField(max_length=3)
    hospital_id=models.ForeignKey(Hospital,on_delete=models.CASCADE, null=True , blank=True, related_name='hospital_id')
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE, null=True , blank=True, related_name='login_id')
class Appointment(models.Model):
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    patient_id = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True, related_name='paitent_id')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True, related_name='doctor_id')
    current_date = models.DateField(auto_now_add=True)
    status=models.CharField(max_length=10,null=True)
    prescription = models.TextField(null=True, blank=True)
