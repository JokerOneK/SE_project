from django.contrib.auth.models import User
from django.db import models

default = [('Cardiologist','Cardiologist'),
           ('Dermatologists','Dermatologists'),
           ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
           ('Allergists/Immunologists','Allergists/Immunologists'),
           ('Anesthesiologists','Anesthesiologists'),
           ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
           ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    department = models.CharField(max_length=50, choices=default, default='Dermatologists')


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    contact_details = models.CharField(max_length=200)


# Create your models here.
