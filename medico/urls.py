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
]
