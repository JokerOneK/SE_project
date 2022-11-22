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
            doc_id = Doctor.objects.get(user=self.user)
            data['id'] = doc_id.id
            data['role'] = 'doctor'
        patients_users = Patient.objects.filter(user=self.user)
        if len(patients_users) > 0:
            patient_id = Patient.objects.get(user=self.user)
            data['id'] = patient_id.id
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


class DoctorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Doctor
        fields = '__all__'

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

        department = Department.objects.create()
        doctor = Doctor.objects.create(
            user=user.id,
            name=validated_data['name'],
            surname=validated_data['surname'],
            middle_name=validated_data['middle_name'],
            address=validated_data['address'],
            phone_number=validated_data['contact_number'],
            department=department,
            date_of_birth=validated_data['date_of_birth'],
            iin=validated_data['iin'],
            experience=validated_data['experience'], #
            category=validated_data['category'], #
            price=validated_data['price'], #
            schedule_details=validated_data['schedule_details'], #
            degree=validated_data['degree'], #
            rating=validated_data['rating'], #
            homepage_url=validated_data['homepage_url'], #
        )
        doctor.save()

        return doctor


class PatientRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Patient
        fields = '__all__'

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
        patient = Patient.objects.create(
            user=user,
            name=validated_data['name'],
            surnam=validated_data['surname'],
            middle_name=validated_data['middle_name'],
            address=validated_data['address'],
            phone_number=validated_data['contact_number'],
            date_of_birth=validated_data['date_of_birth'],
            iin=validated_data['iin'],
            blood_group=validated_data['blood_group'], #
            emergency_phone_number=validated_data['caregiverPhone'],
            email=validated_data['email'],
            contact_details=validated_data['contact_details'], #
            is_married=validated_data['is_married'], #
        )
        patient.save()

        return patient