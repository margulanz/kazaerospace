from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from trainer.models import Trainer

from .models import Schedule, Appointment
from .serializers import ScheduleSerializer, AppointmentSerializer


class GetTrainerSchedule(APIView):
    def get(self, request, trainer_id, **kwargs):
        trainer = Trainer.objects.filter(id=trainer_id).first()
        if trainer:
            schedule = Schedule.objects.get(trainer=trainer)
            serializer = ScheduleSerializer(schedule)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Такого тренера нет в базе данных", status=status.HTTP_404_NOT_FOUND)


class GetAppointment(APIView):
    def get(self, request, trainer_id, **kwargs):
        trainer = Trainer.objects.filter(id=trainer_id).first()
        if trainer:
            appointment = Appointment.objects.filter(trainer=trainer).values()
            # serializer = AppointmentSerializer(appointment)
            return Response(appointment, status=status.HTTP_200_OK)
        return Response("Такого тренера нет в базе данных", status=status.HTTP_404_NOT_FOUND)
