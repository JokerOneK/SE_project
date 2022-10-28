from django.contrib.auth.models import User
from django.db import models

default = [('Cardiologist','Cardiologist'),
           ('Dermatologists','Dermatologists'),
           ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
           ('Allergists/Immunologists','Allergists/Immunologists'),
           ('Anesthesiologists','Anesthesiologists'),
           ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
           ]

default_categories = [('Highest', 'Highest'), ('First', 'First'), ('Second', 'Second')]
default_degree = [('PhD', 'PhD'), ('MD', 'MD'), ('Bachelor', 'Bachelor')]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    department = models.CharField(max_length=50, choices=default, default='Dermatologists')
    date_of_birth = models.DateField()
    iin = models.CharField(max_length=12)
    experience = models.IntegerField()
    #photo = models.ImageField()
    category = models.CharField(max_length=50, choices=default_categories, default='First')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    schedule_details = models.CharField(max_length=200)
    degree = models.CharField(max_length=15, choices=default_degree, default='Bachelor')
    rating = models.PositiveIntegerField()
    homepage_url = models.CharField(max_length=200, null=True)


class Patient(models.Model):
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    iin = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=14, blank=True, default=None)
    emergency_phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True)
    contact_details = models.CharField(max_length=200)
    is_married = models.BooleanField(default=False)


# Create your models here.
