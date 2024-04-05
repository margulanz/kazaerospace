from django.contrib import admin
from .models import Appointment, AvailableTimeSlot, Schedule


admin.site.register(Appointment)
# admin.site.register(AvailableTimeSlot)
admin.site.register(Schedule)
