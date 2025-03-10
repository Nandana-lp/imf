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
    patient_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    date_of_birth = models.CharField(max_length=15)
    contact = models.CharField(max_length=15)
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE, null=True, blank=True,related_name='patient')
    MR = models.CharField(max_length=20, null=True)
    def save(self, *args, **kwargs):
        if not self.MR:
            last_patient = Patient.objects.all().order_by('MR').last()
            if last_patient:
                last_number = int(last_patient.MR.replace('MC', ''))
                new_patient_id = f'MC{str(last_number + 1).zfill(4)}'
            else:
                new_patient_id = 'MC0001'
            self.MR = new_patient_id

        super().save(*args, **kwargs)

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
    patient_id = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True, related_name='patient_id')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True, related_name='doctor_id')
    current_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, null=True)
    prescription = models.TextField(max_length=200, null=True, blank=True)

class PatientTransfer(models.Model):
    current_date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    from_hospital = models.ForeignKey(Hospital, related_name='from_hospital', on_delete=models.CASCADE, null=True)
    to_hospital = models.ForeignKey(Hospital, related_name='to_hospital', on_delete=models.CASCADE)

class Ambulance(models.Model):
    ambulance_category = models.CharField(max_length=20)
    vehicle_type= models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=20)
    driver_name= models.CharField(max_length=50) 
    contact=models.CharField(max_length=10)
    hosp_id=models.ForeignKey(Hospital,on_delete=models.CASCADE, null=True , blank=True, related_name='hosp_id')
    log_id=models.ForeignKey(Login,on_delete=models.CASCADE, null=True , blank=True, related_name='log_id')
