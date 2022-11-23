from django.urls import path
from .views import doctor_views, views, patient_views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('admin/doctor/', doctor_views.DoctorUpdateAdmin.as_view(), name='doctor_register'),
    path('', views.getRoutes),
    path('appointments_doctor/', doctor_views.doctor_appointments_list),
    path('appointments_patient/', patient_views.patients_appointments_list),
    path('appointments/<int:pk>/', views.appointment_detail),
    path('departments/', views.department_list),
    path('patients/', patient_views.PatientList.as_view()),
    path('patients/<int:pk>/', patient_views.PatientDetail.as_view()),
    path('patients/update/<int:pk>/', patient_views.PatientUpdate.as_view()),
    path('patients/admin/update/<int:pk>/', patient_views.PatientUpdateAdmin.as_view()),
    path('doctors/', doctor_views.DoctorList.as_view()),
    path('doctors/<int:pk>/', doctor_views.DoctorDetail.as_view()),
    path('doctors/update/<int:pk>/', doctor_views.DoctorUpdate.as_view()),
    path('doctors/admin/update/<int:pk>/', doctor_views.DoctorUpdateAdmin.as_view()),
]
