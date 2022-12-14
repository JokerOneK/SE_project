from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from hospital.serializer import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from hospital.models import *
from hospital.serializers import *


# Create your views here.

class CustomUpdatePermission(permissions.BasePermission):
    """
    Permission class to check that a user can update his own resource only
    """


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
    ]
    return Response(routes)


from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


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


@permission_classes([AllowAny])
class DepartmentDetail(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = "slug"





@permission_classes([AllowAny])
class FreeAppointmentList(APIView):
    def get(self, request):
        doctor = self.request.query_params["username"]
        date = self.request.query_params["date"]
        queryset = Appointment.objects.filter(doctor__user__username=doctor, date=date)

        free_timeslots = [j for j in range(9)]

        for i in queryset:
            if i.timeslot in free_timeslots:
                free_timeslots.remove(i.timeslot)
        return Response(free_timeslots)

@permission_classes([AllowAny])
class AppointmentList(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


@permission_classes([IsAuthenticated])
class AppointmentCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# SERVICES
@permission_classes([AllowAny])
class ServicesList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

@permission_classes([AllowAny])
class ServicesDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "slug"



