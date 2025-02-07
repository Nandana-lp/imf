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
    if request.method=="POST":
        form=PatientForm(request.POST)
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user=login.save(commit=False)
            user.user_type='patient'
            user.save()
            a=form.save(commit=False)
            a.login_id=user
            a.save()
            messages.success(request,"Patient registered successfull")
    else:
        form=PatientForm()
        login=LoginForm()
    return render(request,'registration.html',{'form':form,'login':login})


def HospitalHome(request):
    return render(request,'hospital.html')

def PatientHome(request):
    return render(request,'patienthome.html')

def DoctorHome(request):
    return render(request,'doctorhome.html')

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
        return render(request, 'doc.html')

def patient_appointment(request,id):
    p_id=request.session['patient_id']
    p=get_object_or_404(Login,id=p_id)
    q=get_object_or_404(Doctor,id=id)
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.patient_id=p
            a.doctor_id=q
            a.save()
            messages.success(request,"Requested for Appointment")
            return redirect('PatientHome')
    else:
        form=AppointmentForm()
    return render(request,'appointment.html',{'form':form})   
    

