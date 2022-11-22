from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('admin/patient/', views.PatientRegisterView.as_view(), name='patient_register'),
    path('admin/doctor/', views.DoctorRegisterView.as_view(), name='doctor_register'),
    path('', views.getRoutes),
    path('appointments/', views.AppointmentList.as_view()),
    path('appointments/<int:pk>/', views.appointment_detail),
    path('departments/', views.department_list),
    path('patients/', views.PatientList.as_view()),
    path('patients/<int:pk>/', views.PatientDetail.as_view()),
    path('doctors/', views.DoctorList.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view()),
    path('doctors/update/<int:pk>/', views.DoctorUpdate.as_view()),
    path('appointments/doctor/', views.doctor_appointments_list),
]
