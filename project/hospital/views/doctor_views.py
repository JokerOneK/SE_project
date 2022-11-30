## DOCTORS
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from hospital.models import *
from hospital.serializers import DoctorSerializer, AppointmentSerializer
from hospital.views.views import CustomUpdatePermission


@permission_classes([AllowAny])
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@permission_classes([AllowAny])
class DoctorDetail(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = "slug"

@permission_classes([IsAuthenticated, CustomUpdatePermission])
class DoctorUpdate(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = "slug"

@permission_classes([IsAuthenticated, IsAdminUser])
class DoctorUpdateAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = "slug"


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_appointments_list(request):
    """
    List booked appointments for particular doctor.
    """
    if request.method == 'GET':
        print(request.query_params)
        appointments = Appointment.objects.filter(doctor__user__username=request.query_params["username"])
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)