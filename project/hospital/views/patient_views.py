from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from hospital.models import *
from hospital.serializers import PatientSerializer, AppointmentSerializer
from hospital.views.views import CustomUpdatePermission




@permission_classes([IsAdminUser, IsAuthenticated])
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@permission_classes([ IsAuthenticated])
class PatientDetail(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "slug"


@permission_classes([CustomUpdatePermission, IsAuthenticated])
class PatientUpdate(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "slug"

@permission_classes([IsAdminUser, IsAuthenticated])
class PatientUpdateAdmin(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "slug"


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patients_appointments_list(request):
    """
    List booked appointments for particular doctor.
    """
    if request.method == 'GET':
        print(request.query_params)
        appointments = Appointment.objects.filter(patient__user__username=request.query_params["username"])
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)