from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from autoslug import AutoSlugField

default = [('Medicine','Medicine'),
           ('Surgery','Surgery'),
           ('Gynecology','Gynecology'),
           ('Obstetrics','Obstetrics'),
           ('Pediatrics','Pediatrics'),
           ('Radiology','Radiology'),
           ('Eye','Eye'),
           ('ENT','ENT'),
           ('Dental','Dental'),
           ('Orthopedics','Orthopedics'),
           ('Neurology','Neurology'),
           ('Cardiology','Cardiology'),
           ('Psychiatry','Psychiatry'),
           ('Scin','Scin'),
           ]

default_services = (
    (
        ('Surgery', (
            ('Laparoscopic procedures', 'Laparoscopic procedures'),
            ('Bed, free food, investigations', 'Bed, free food, investigations'),
            ('Robotic Surgeries', 'Robotic Surgeries'),
            ('Endoscopic procedures', 'Endoscopic procedures'),
        ))
    ),
    (
        ('Obstetrics' , (
            ('Pregnancy care', 'Pregnancy care'),
            ('Surgical procedures', 'Surgical procedures'),
            ('Specialty care', 'Specialty care'),
            ('Prenatal yoga classes','Prenatal yoga classes')
        ))
    ),
    (
        ('Pediatrics' , (
            ('Pediatricians', 'Pediatricians'),
            ('Pediatric neurologist', 'Pediatric neurologist'),
            ('Pediatric ophthalmologist', 'Pediatric ophthalmologist'),
            ('Ultrasound doctor', 'Ultrasound doctor')
        ))
    ),
    (
        ('Radiology' , (
            ('X-ray', 'X-ray'),
            ('Ultrasound', 'Ultrasound'),
            ('Computed tomography', 'Computed tomography'),
            ('Magnetic resonance imaging','Magnetic resonance imaging')
        ))
    ),
    (
        ('Eye', (
            ('Visual field test', 'Visual field test'),
            ('Laser treatment for specific eye problems', 'Laser treatment for specific eye problems'),
            ('Cataract', 'Cataract'),
            ('General ophthalmology', 'General ophthalmology')
        ))
    ),
    (
        ('ENT' , (
            ('Foreign body removal', 'Foreign body removal'),
            ('Endoscopic surgeries for nose',  'Endoscopic surgeries for nose'),
            ('Biopsies of suspicious mass', 'Biopsies of suspicious mass'),
            ('Diagnostic endoscopic examination', 'Diagnostic endoscopic examination')
        ))
    ),
    (
        ('Dental' , (
            ('Cosmetic dentistry', 'Cosmetic dentistry'),
            ('Dental cleanings', 'Dental cleanings'),
            ('Orthodontics',  'Orthodontics'),
            ('Implants', 'Implants')
        ))
    ),
    (
        ('Orthopedics' , (
            ('Bone scans', 'Bone scans'),
            ('Computed tomography',  'Computed tomography'),
            ('Arthrogram',  'Arthrogram'),
            ('Discography', 'Discography')
        ))
    ),
    (
        ('Neurology' , (
            ('Electrophysiological investigations', 'Electrophysiological investigations'),
            ('Epilepsy surgery', 'Epilepsy surgery'),
            ('Botulinum Toxin', 'Botulinum Toxin'),
            ('Stroke thrombolysis', 'Stroke thrombolysis')
        ))
    ),
    (
        ('Cardiology', (
            ('Implantable cardiac devices', 'Implantable cardiac devices'),
            ('Cardioverter defibrillators',  'Cardioverter defibrillators'),
            ('Ventricular assist devices', 'Ventricular assist devices'),
            ('Catheter ablation', 'Catheter ablation')
        ))
    )
)
default_categories = [('Highest', 'Highest'), ('First', 'First'), ('Second', 'Second')]
default_degree = [('PhD', 'PhD'), ('MD', 'MD'), ('Bachelor', 'Bachelor')]

class Department(models.Model):
    name = models.CharField(max_length=50, choices=default, default='Dermatologists')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='doctors')
    date_of_birth = models.DateField()
    iin = models.CharField(max_length=12)
    experience = models.IntegerField()
    photo = models.ImageField(blank=True)
    category = models.CharField(max_length=50, choices=default_categories, default='First')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    schedule_details = models.CharField(max_length=200)
    degree = models.CharField(max_length=15, choices=default_degree, default='Bachelor')
    rating = models.PositiveIntegerField()
    homepage_url = models.CharField(max_length=200, null=True)
    slug = AutoSlugField(populate_from='doctor_username')

    @property
    def doctor_username(self):
        return self.user.username

    def __str__(self):
        return f"{self.name}, {self.surname}"


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
    slug = AutoSlugField(populate_from='patient_username')

    @property
    def patient_username(self):
        return self.user.username

    def __str__(self):
        return f"{self.name}, {self.surname}"


class Appointment(models.Model):
    """Contains info about appointment"""

    class Meta:
        unique_together = ('doctor', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )

    doctor = models.ForeignKey('Doctor',on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctor, self.patient.name)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]


class Service(models.Model):
    name = models.CharField(max_length=200, choices=default_services, default="X-ray")
    price = models.PositiveIntegerField(validators=[MaxValueValidator(10000000000)])
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='services')
    doctor = models.ManyToManyField(Doctor)
    contradictions = models.CharField(max_length=200)
    pre_procedure = models.CharField(max_length=50)

    def __str__(self):
        return self.name
