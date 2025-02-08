from django.shortcuts import render,redirect,get_object_or_404
from .forms import HospitalForm, LoginForm ,PatientForm,LoginCheckForm,DoctorForm,AppointmentForm
from django.contrib import messages
from .models import Hospital ,Login ,Patient,Doctor,Appointment
from django.db.models import Q

def index(request):
    return render(request,'index.html')
def adminform(request):
    return render(request,'adminform.html')
def login(request):
    return render(request,'login.html')

def HospitalReg(request):
    if request.method=="POST":
        form=HospitalForm(request.POST)
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user=login.save(commit=False)
            user.user_type='hospital'
            user.save()
            a=form.save(commit=False)
            a.login_id=user
            a.save()
            messages.success(request,"Hospital registered successfull")
    else:
        form=HospitalForm()
        login=LoginForm()
    return render(request,'registration.html',{'form':form,'login':login})
def PatientReg(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        login = LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user = login.save(commit=False)
            user.user_type = 'patient'
            user.save()
            a = form.save(commit=False)
            a.login_id = user
            a.save()
            messages.success(request, "Patient registered successfully")
    else:
        form = PatientForm()
        login = LoginForm()
    return render(request, 'registration.html', {'form': form, 'login': login})


def HospitalHome(request):
    return render(request,'hospital.html')

def PatientHome(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login')
    login = get_object_or_404(Login, id=patient_id)
    patient = get_object_or_404(Patient, login_id=login)
    appointments = Appointment.objects.filter(patient_id=patient)
    return render(request, 'patienthome.html', {'appointments': appointments})


def DoctorHome(request):
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        return redirect('login')
    login = get_object_or_404(Login, id=doctor_id)
    doctor = get_object_or_404(Doctor, login_id=login)
    appointments = Appointment.objects.filter(doctor_id=doctor)
    return render(request, 'doctorhome.html', {'appointments': appointments})

def LoginCheck(request):
    if request.method=='POST':
        form=LoginCheckForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=Login.objects.get(email=username)
                if user.password==password:
                  if user.user_type=='hospital':
                    request.session['hospital_id']=user.id
                    return redirect('HospitalHome')
                  elif user.user_type=='patient':
                    request.session['patient_id']=user.id
                    return redirect('PatientHome')
                  elif user.user_type=='doctor':
                    request.session['doctor_id']=user.id
                    return redirect('doctor_home')
                else:
                    messages.error(request,'Invalid Password')   
            except Login.DoesNotExist:
                messages.error(request,'User Does Not Exist')
    else:
        form=LoginCheckForm()
    return render(request,'login.html',{'form':form})
def AddDoctor(request):
    id=request.session['hospital_id']
    user=get_object_or_404(Login,id=id)
    hospital=get_object_or_404(Hospital,login_id=user)
    if request.method=='POST':
        form=DoctorForm(request.POST)  
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            a=login.save()
            a.user_type='doctor'
            a.save()
            doc=form.save(commit=False)
            doc.hospital_id=hospital
            doc.login_id=a
            doc.save()
            messages.success(request,'Added Doctor successfully')
            return redirect('HospitalHome')
    else:
        form=DoctorForm()
        login=LoginForm() 
    return render(request,'add_doc.html',{'form':form,'login':login})
def ViewDoctor(request):
    doctors=Doctor.objects.all()
    return render(request,'doclist.html',{'doctors':doctors}) 

def search_doctor(request):
    if request.method == "POST":
        query = request.POST.get('specialization')
        users = Doctor.objects.filter(
                Q(doctor_name__icontains=query) |
                Q(specialization__icontains=query) |
                Q(gender__icontains=query)
        )
        return render(request, 'doc.html', {'users':users})
    else:
        doctors = Doctor.objects.all()  # No query, show all doctors
    return render(request, 'doclist.html', {'doctors': doctors, 'query': a})


def patient_appointment(request, id):
    p_id = request.session.get('patient_id')
    login = get_object_or_404(Login, id=p_id)
    patient = get_object_or_404(Patient, login_id=login)  # Correctly get the Patient instance
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient_id = patient  # Assign the Patient instance
            appointment.doctor_id = doctor
            appointment.save()
            messages.success(request, "Requested for Appointment")
            return redirect('PatientHome')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully")
            return redirect('PatientHome')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'edit_appointment.html', {'form': form})

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    messages.success(request, "Appointment cancelled successfully")
    return redirect('PatientHome')
