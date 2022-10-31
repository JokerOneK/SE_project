from django.contrib import admin
from .models import Doctor, Patient


# Register your models here.
# listings/admin.py

admin.site.register(Doctor)

admin.site.register(Patient)

# @admin.register(Doctor)
# class RequestDemoAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in
#                     Doctor._meta.get_fields()]
#     # list_editable = [field.name for field in
#     #                  Doctor._meta.get_fields()]
#     # fields = [field.name for field in
#     #           Doctor._meta.get_fields()]
#
# @admin.register(Patient)
# class RequestDemoAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in
#                     Patient._meta.get_fields()]
#     #
#     # list_editable = [field.name for field in
#     #                  Patient._meta.get_fields()]
#
#     # fields = [field.name for field in
#     #           Patient._meta.get_fields()]