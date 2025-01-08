from django.contrib import admin
from appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appointment_type', 'appointment_status', 'time', 'cancel']

    def patient_name(self, obj):
        return obj.patient.user.username

    def doctor_name(self, obj):
        return obj.doctor.user.username

admin.site.register(Appointment, AppointmentAdmin)