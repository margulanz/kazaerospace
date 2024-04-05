from django.contrib import admin
from .models import Appointment, AvailableTimeSlot, Schedule


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['trainer', 'client', 'date', 'timeslot', 'room']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['trainer']
    readonly_fields = ('trainer',)


admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(AvailableTimeSlot)
admin.site.register(Schedule, ScheduleAdmin)
