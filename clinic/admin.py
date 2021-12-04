from django.contrib import admin
from .models import Clinic

# Register your models here.

class ClinicAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_phone', 'patient_address', 'patient_case', 'drug', 'doctor','datetime']
    list_filter = ['patient_address', 'patient_case', 'doctor', 'datetime']
    search_fields = ['patient_name']

admin.site.register(Clinic, ClinicAdmin)