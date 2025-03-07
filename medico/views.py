from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    HospitalForm, LoginForm, PatientForm, LoginCheckForm, 
    DoctorForm, AppointmentForm, PrescriptionForm, MRIForm
)
from django.contrib import messages
from .models import Hospital ,Login ,Patient,Doctor,Appointment,PatientTransfer
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def adminform(request):
    return render(request, 'adminform.html')

def login(request):
    return render(request, 'login.html')

def HospitalReg(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        login = LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user = login.save(commit=False)
            user.user_type = 'hospital'
            user.save()
            hospital = form.save(commit=False)
            hospital.login_id = user
            hospital.save()
            messages.success(request, "Hospital registered successfully")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = HospitalForm()
        login = LoginForm()
    return render(request, 'registration.html', {'form': form, 'login': login})

def PatientReg(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        login = LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user = login.save(commit=False)
            user.user_type = 'patient'
            user.save()
            patient = form.save(commit=False)
            patient.login_id = user
            patient.save()
            messages.success(request, "Patient registered successfully")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PatientForm()
        login = LoginForm()
    return render(request, 'registration.html', {'form': form, 'login': login})

def HospitalHome(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    return render(request, 'hospital.html')

def PatientHome(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    login = get_object_or_404(Login, id=patient_id)
    # print(login)
    patient = get_object_or_404(Patient, login_id=login)
    appointments = Appointment.objects.filter(patient_id=login.id)  
    
    print("appointments..", appointments)
    
    return render(request, 'patienthome.html', {'appointments': appointments})

def DoctorHome(request):
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    appointments = Appointment.objects.filter(doctor_id=doctor_id)
    return render(request, 'doctorhome.html', {'appointments': appointments})

def LoginCheck(request):
    if request.method == 'POST':
        form = LoginCheckForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Login.objects.get(email=email)
                if user.password == password:
                    request.session[f'{user.user_type}_id'] = user.id
                    return redirect(f'{user.user_type.capitalize()}Home')
                else:
                    messages.error(request, 'Invalid Password')
            except Login.DoesNotExist:
                messages.error(request, 'User Does Not Exist')
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = LoginCheckForm()
    return render(request, 'login.html', {'form': form})

def AddDoctor(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        login = LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user = login.save(commit=False)
            user.user_type = 'doctor'
            user.save()
            doctor = form.save(commit=False)
            doctor.hospital_id = hospital
            doctor.login_id = user
            doctor.save()
            messages.success(request, 'Doctor added successfully')
            return redirect('HospitalHome')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = DoctorForm()
        login = LoginForm()
    return render(request, 'add_doc.html', {'form': form, 'login': login})

def ViewDoctor(request):
    hospital_id = request.session.get('hospital_id')
    if not hospital_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    doctors = Doctor.objects.filter(hospital_id=hospital_id)
    return render(request, 'doclist.html', {'doctors': doctors})

def search_doctor(request):
    if request.method == "POST":
        query = request.POST.get('specialization')
        doctors = Doctor.objects.filter(
            Q(doctor_name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(gender__icontains=query)
        )
        if not doctors.exists():
            messages.info(request, "No doctors found matching the criteria.")
        return render(request, 'doc.html', {'doctors': doctors})
    else:
        doctors = Doctor.objects.all()  # No query, show all doctors
    return render(request, 'doclist.html', {'doctors': doctors, 'query': a})


def patient_appointment(request, doctor_id):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient_id = login # Assign the Patient instance
            appointment.doctor_id = doctor 
            appointment.status="confirmed"
            appointment.save()
        
            messages.success(request, "Requested for Appointment")
            return redirect('PatientHome')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form, 'doctor': doctor})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    # Ensure only authorized users can edit this appointment
    patient_id = request.session.get('patient_id')
    if appointment.patient_id.id != patient_id:
        messages.error(request, "You are not authorized to edit this appointment.")
        return redirect('PatientHome')

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully.")
            return redirect('PatientHome')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'edit_appointment.html', {'form': form})

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    patient_id = request.session.get('patient_id')
    if appointment.patient_id.id != patient_id:
        messages.error(request, "You are not authorized to cancel this appointment.")
        return redirect('PatientHome')

    appointment.status = "cancelled"
    appointment.save()
    messages.success(request, "Appointment cancelled successfully.")
    return redirect('PatientHome')

def add_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    doctor_id = request.session.get('doctor_id')
    if appointment.doctor_id.id != doctor_id:
        messages.error(request, "You are not authorized to add prescriptions for this appointment.")
        return redirect('doctor_home')

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request,"Prescription added successfully")
            return redirect('/doctor_home')
    else:
        form=PrescriptionForm(instance=appointment)
    return render(request,'add_prescription.html',{'form':form,'appointment':appointment})


def view_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    # Ensure only authorized users (patient/doctor) can view the prescription
    user_id = request.session.get('patient_id') or request.session.get('doctor_id')
    if appointment.patient_id.login_id.id != user_id and appointment.doctor_id.login_id.id != user_id:
        messages.error(request, "You are not authorized to view this prescription.")
        return redirect('login')

    return render(request, 'view_prescription.html', {'appointment': appointment})

def search_patient(request):
    if request.method == 'POST':
        query = request.POST.get('mri_number')
        results = Patient.objects.filter(Q(MRI__icontains=query))
        if not results.exists():
            messages.info(request, "No patients found with the given MRI number.")
        return render(request, 'search_patient.html', {'results': results})
    else:
        return render(request, 'search_patient.html')

def search_hospital(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        results = Hospital.objects.filter(
            Q(hospital_name__icontains=query) | Q(city__icontains=query)
        )
        if not results.exists():
            messages.info(request, "No hospitals found matching the search criteria.")
        return render(request, 'search_hospital.html', {'results': results})
    else:
        return render(request, 'search_hospital.html')

# View for transferring patients
def transfer_patient(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if request.method == 'POST':
        mri_number = request.POST.get('mri_number')
        patient_results = Patient.objects.filter(Q(MRI__icontains=mri_number))
        if not patient_results.exists():
            messages.error(request, "No matching patients found.")
        return render(request, 'transfer_patient.html', {
            'hospital': hospital,
            'patients': patient_results
        })
    return render(request, 'transfer_patient.html', {'hospital': hospital})

def transfer_patient_action(request, patient_id, to_hospital_id):
    # Assume the hospital initiating the transfer is from the session
    from_hospital_id = request.session.get('hospital_id')
    if not from_hospital_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')

    # Fetching required hospital and patient objects
    from_hospital = get_object_or_404(Hospital, id=from_hospital_id)
    to_hospital = get_object_or_404(Hospital, id=to_hospital_id)
    patient = get_object_or_404(Patient, id=patient_id)
    to_hospital = get_object_or_404(Hospital, id=hosp_id)
    from_hospital = patient.hsp_id  
    if from_hospital and from_hospital != to_hospital:
        PatientTransfer.objects.create(patient=patient, from_hospital=from_hospital, to_hospital=to_hospital)
        patient.hsp_id = to_hospital
        patient.save()
        messages.success(request, "Patient transferred successfully.")
    else:
        messages.error(request, "Transfer not possible.")
    return redirect('transfer_patient', id=hosp_id)

