## DOCTORS
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from hospital.models import *
from hospital.serializers import DoctorSerializer
from hospital.views.views import CustomUpdatePermission


@permission_classes([AllowAny])
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@permission_classes([IsAuthenticated])
class DoctorDetail(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@permission_classes([IsAuthenticated, CustomUpdatePermission])
class DoctorUpdate(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@permission_classes([IsAuthenticated, IsAdminUser])
class DoctorUpdateAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer