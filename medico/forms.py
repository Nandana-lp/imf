from django import forms
from .models import Login, Hospital, Patient, Doctor, Appointment, Ambulance

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Login
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name', 'contact', 'city', 'state', 'district']
        widgets = {
            'hospital_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name', 'address', 'gender', 'date_of_birth', 'contact']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginCheckForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_name', 'contact', 'specialization', 'gender', 'age']
        widgets = {
            'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['prescription']
        widgets = {
            'prescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter prescription here...'}),
        }

class MRForm(forms.Form):
    mr_number = forms.CharField(max_length=20, label='MR Number', widget=forms.TextInput(attrs={'class': 'form-control'}))

category=[
        ('Intensive Care Unit','Intensive Care Unit'),
        ('Basic Life Support','Basic Life Support'),
        ('Advanced Life Support','Advanced Life Support'),
        ('Air Ambulance','Air Ambulance'),
        ('Patient Transport','Patient Transport')
    ]
class AmbulanceForm(forms.ModelForm):
    ambulance_category=forms.ChoiceField(choices=category)
    class Meta:
        model=Ambulance
        fields=['ambulance_category','vehicle_type','vehicle_number','driver_name','contact']
        widgets = {
            'ambulance_category': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LoginEditForm(forms.ModelForm):
     class Meta:
        model = Login
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
