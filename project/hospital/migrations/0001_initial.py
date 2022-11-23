# Generated by Django 4.1.2 on 2022-11-23 10:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Medicine', 'Medicine'), ('Surgery', 'Surgery'), ('Gynecology', 'Gynecology'), ('Obstetrics', 'Obstetrics'), ('Pediatrics', 'Pediatrics'), ('Radiology', 'Radiology'), ('Eye', 'Eye'), ('ENT', 'ENT'), ('Dental', 'Dental'), ('Orthopedics', 'Orthopedics'), ('Neurology', 'Neurology'), ('Cardiology', 'Cardiology'), ('Psychiatry', 'Psychiatry'), ('Scin', 'Scin')], default='Dermatologists', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10000000000)])),
                ('contradictions', models.CharField(max_length=200)),
                ('pre_procedure', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='hospital.department')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('iin', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=20)),
                ('blood_group', models.CharField(blank=True, default=None, max_length=14)),
                ('emergency_phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact_details', models.CharField(max_length=200)),
                ('is_married', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
                ('date_of_birth', models.DateField()),
                ('iin', models.CharField(max_length=12)),
                ('experience', models.IntegerField()),
                ('category', models.CharField(choices=[('Highest', 'Highest'), ('First', 'First'), ('Second', 'Second')], default='First', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('schedule_details', models.CharField(max_length=200)),
                ('degree', models.CharField(choices=[('PhD', 'PhD'), ('MD', 'MD'), ('Bachelor', 'Bachelor')], default='Bachelor', max_length=15)),
                ('rating', models.PositiveIntegerField()),
                ('homepage_url', models.CharField(max_length=200, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='hospital.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='YYYY-MM-DD')),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 – 09:30'), (1, '10:00 – 10:30'), (2, '11:00 – 11:30'), (3, '12:00 – 12:30'), (4, '13:00 – 13:30'), (5, '14:00 – 14:30'), (6, '15:00 – 15:30'), (7, '16:00 – 16:30'), (8, '17:00 – 17:30')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
            options={
                'unique_together': {('doctor', 'date', 'timeslot')},
            },
        ),
    ]
