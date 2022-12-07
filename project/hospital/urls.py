from django.urls import path
from .views import doctor_views, views, patient_views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('admin/doctor/<slug:slug>/', doctor_views.DoctorUpdateAdmin.as_view(), name='doctor_register'),

    # Appointments
    path('appointments_create/', views.AppointmentCreate.as_view()),
    path('appointments_doctor/', doctor_views.doctor_appointments_list),
    path('appointments_doctor_free/', views.FreeAppointmentList.as_view()),
    path('appointments_patient/', patient_views.patients_appointments_list),
    path('appointments/<int:pk>/', views.appointment_detail),

    # Departments
    path('departments/', views.department_list),
    path('departments/<slug:slug>/', views.DepartmentDetail.as_view()),

    # Patients
    path('patients/', patient_views.PatientList.as_view()),
    path('patients/<slug:slug>/', patient_views.PatientDetail.as_view()),
    path('patients/update/<slug:slug>/', patient_views.PatientUpdate.as_view()),
    path('patients/admin/update/<slug:slug>/', patient_views.PatientUpdateAdmin.as_view()),

    #Doctors
    path('doctors/', doctor_views.DoctorList.as_view()),
    path('doctors/<slug:slug>/', doctor_views.DoctorDetail.as_view()),
    path('doctors/update/<slug:slug>/', doctor_views.DoctorUpdate.as_view()),
    path('doctors/admin/update/<slug:slug>/', doctor_views.DoctorUpdateAdmin.as_view()),

    #Services
    path('services/', views.ServicesList.as_view()),
    path('services/<slug:slug>/', views.ServicesDetail.as_view()),
]

# appointments_create:
#
# in body:
# date,
# timeslot,
# doctor id,
# patient id