from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        # doctor_users = Doctor.objects.filter(user=user)
        # if len(doctor_users) > 0:
        #     token['role'] = 'doctor'
        # patients_users = Patient.objects.filter(user=user)
        # if len(patients_users) > 0:
        #     token['role'] = 'patient'
        #
        # if len(doctor_users) == 0 and len(patients_users) == 0:
        #     token['role'] = 'not_found'

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)   # comment out if you don't want this
        data["access"] = str(refresh.access_token)
        data["email"] = self.user.email
        data['username'] = self.user.username

        doctor_users = Doctor.objects.filter(user=self.user)
        if len(doctor_users) > 0:
            data['role'] = 'doctor'
        patients_users = Patient.objects.filter(user=self.user)
        if len(patients_users) > 0:
            data['role'] = 'patient'

        if self.user.is_superuser:
            data['role'] = 'admin'

        if len(doctor_users) == 0 and len(patients_users) == 0 and not self.user.is_superuser:
            data['role'] = 'not_found'

        return data

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
