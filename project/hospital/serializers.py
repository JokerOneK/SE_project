from .models import *
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'