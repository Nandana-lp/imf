from django import forms
from .models import Login,Hospital,Patient,Doctor,Appointment

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=['hospital_name','contact','city','state','district']
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['patient_name','address','gender','date_of_birth','contact']
class LoginCheckForm(forms.Form):
    email=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['doctor_name','contact','specialization','gender','age']
class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['date','time']
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['prescription']
        widgets = {
            'prescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter prescription here...'}),
        }

