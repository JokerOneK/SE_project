from .models import *
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True)
    services = ServiceSerializer(many=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'doctors', 'slug', 'services')


