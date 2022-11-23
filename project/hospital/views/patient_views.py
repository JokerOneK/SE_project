from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from hospital.models import *
from hospital.serializers import PatientSerializer
from hospital.views.views import CustomUpdatePermission



@permission_classes([IsAdminUser, IsAuthenticated])
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@permission_classes([ IsAuthenticated])
class PatientDetail(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@permission_classes([CustomUpdatePermission, IsAuthenticated])
class PatientUpdate(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

@permission_classes([IsAdminUser, IsAuthenticated])
class PatientUpdateAdmin(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer