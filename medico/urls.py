from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminform/',views.adminform,name='adminform'),
    path('login/',views.login,name='login'),
    path('hospital_reg',views.HospitalReg,name='HospitalReg'),
    path('patient_reg',views.PatientReg,name='patientReg'),
    path('hospital_home',views.HospitalHome,name='HospitalHome'),
    path('patient_home',views.PatientHome,name='PatientHome'),
    path('logincheck',views.LoginCheck,name='LoginCheck'),
    path('add_doc',views.AddDoctor,name='AddDoctor'),
    path('view_doc',views.ViewDoctor,name='ViewDoctor'),
    path('search_doc', views.search_doctor, name='search_doctor'),
    path('patient_appointment/<int:id>',views.patient_appointment,name='patient_appointment'),
    path('doctor_home',views.DoctorHome,name='doctor_home'),
    path('edit_appointment/<int:appointment_id>',views.edit_appointment,name='edit_appointment'),
    path('cancel_appointment/<int:appointment_id>',views.cancel_appointment,name='cancel_appointment'),
   path('add_prescription/<int:appointment_id>/', views.add_prescription, name='add_prescription'),
    path('view_prescription/<int:appointment_id>/', views.view_prescription, name='view_prescription'),
]
