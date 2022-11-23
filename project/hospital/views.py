from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .serializer import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *


# Create your views here.

class CustomUpdatePermission(permissions.BasePermission):
    """
    Permission class to check that a user can update his own resource only
    """

    # def has_permission(self, request, view):
    #     # check that its an update request and user is modifying his resource only
    #     if request.user.is_superuser:
    #         return True
    #     print(view)
    #     if view.kwargs['id'] != request.user.id:
    #         return False # not grant access
    #
    #     return True # grant access otherwise

    def has_object_permission(self, request, view, obj):
        # check that its an update request and user is modifying his resource only
        if request.user.is_superuser:
            return True
        print(f'object = {obj.user}')
        print(f'object.user.id = {obj.user.id}, request.user.id = {request.user.id}')
        if obj.id != request.user.id:
            return False # not grant access

        return True # grant access otherwise


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class DoctorRegisterView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = DoctorRegisterSerializer


class PatientRegisterView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = PatientRegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/admin/doctor/',
        '/api/admin/patient/',
        '/api/appointments/',
        '/api/appointments/<int:pk>/',
        '/api/departments/',
        '/api/patients/',
        '/api/patients/<int:pk>/',
        '/api/doctors/',
        '/api/doctors/<int:pk>/',
        '/api/services/',
        '/api/services/<int:pk>/',
    ]
    return Response(routes)


from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def testEndPoint(request):
#     if request.method == 'GET':
#         data = f"Congratulation {request.user}, your API just responded to GET request"
#         return Response({'response': data}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         text = request.POST.get('text')
#         data = f'Congratulation your API just responded to POST request with text: {text}'
#         return Response({'response': data}, status=status.HTTP_200_OK)
#     return Response({}, status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def appointments_list(request):
#     """
#     List all Appointments.
#     """
#     if request.method == 'GET':
#         appointments = Appointment.objects.all()
#         serializer = AppointmentSerializer(appointments, many=True)
#         return Response(serializer.data)


@csrf_exempt
@permission_classes([IsAuthenticated])
def appointment_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AppointmentSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AppointmentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
@permission_classes([AllowAny])
def department_list(request):
    """
    List all Appointments.
    """
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


## PATIENTS
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

## DOCTORS
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


@permission_classes([IsAuthenticated])
class AppointmentList(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


@permission_classes([IsAuthenticated, IsAdminUser])
class AppointmentList(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# SERVICES
@permission_classes([AllowAny])
class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

@permission_classes([IsAuthenticated])
class ServicesDetail(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_appointments_list(request):
    """
    List booked appointments for particular doctor.
    """
    if request.method == 'GET':
        appointments = Appointment.objects.filter(doctor__name=request.data["name"])
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)