from django import forms
from .models import Login, Hospital, Patient, Doctor, Appointment

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

class MRIForm(forms.Form):
    mri_number = forms.CharField(max_length=20, label='MRI Number', widget=forms.TextInput(attrs={'class': 'form-control'}))