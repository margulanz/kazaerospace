from rest_framework import serializers
from .models import Schedule, AvailableTimeSlot, Appointment


class AvailableTimeSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailableTimeSlot
        exclude = ("id",)


class ScheduleSerializer(serializers.ModelSerializer):
    available_timeslots = AvailableTimeSlotSerializer(many=True)

    class Meta:
        model = Schedule
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
