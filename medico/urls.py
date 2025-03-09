from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminform/', views.adminform, name='adminform'),
    path('login/', views.login, name='login'),
    path('hospital_reg', views.HospitalReg, name='HospitalReg'),
    path('patient_reg', views.PatientReg, name='patientReg'),
    path('hospital_home', views.HospitalHome, name='HospitalHome'),
    path('patient_home', views.PatientHome, name='PatientHome'),
    path('logincheck', views.LoginCheck, name='LoginCheck'),

    path('add_doc', views.AddDoctor, name='AddDoctor'),
    path('view_doc', views.ViewDoctor, name='ViewDoctor'),
    path('search_doc', views.search_doctor, name='search_doctor'),

    path('patient_appointment/<int:id>', views.patient_appointment, name='patient_appointment'),
    path('DoctorHome', views.DoctorHome, name='DoctorHome'),
    path('edit_appointment/<int:appointment_id>', views.edit_appointment, name='edit_appointment'),
    path('cancel_appointment/<int:appointment_id>', views.cancel_appointment, name='cancel_appointment'),
    path('add_prescription/<int:appointment_id>/', views.add_prescription, name='add_prescription'),
    path('view_prescription/<int:appointment_id>/', views.view_prescription, name='view_prescription'),
    
    path('search_hospital', views.search_hospital, name='search_hospital'),
    path('search_patient', views.search_patient, name='search_patient'),

    path('find_patient/<int:hsp_id>', views.find_patient, name='find_patient'),
    path('transfer_patient/<int:id>/<int:patient_id>' , views.transfer_patient, name='transfer_patient'),
    path('transferred_patients', views.transferred_patients, name='transferred_patients'),
    path('transfer_view_patients',views.transfer_view_patients,name='transfer_view_patients'),

    path('AddAmbulance',views.AddAmbulance,name='AddAmbulance'),
    path('AmbulanceHome',views.AmbulanceHome,name='AmbulanceHome'),

    path('edit_ambulance', views.edit_ambulance,name='edit_ambulance'),
    path('edit_hospital', views.edit_hospital,name='edit_hospital'),
    path('edit_doctor', views.edit_doctor,name='edit_doctor'),
    path('edit_patient', views.edit_patient,name='edit_patient'),


]