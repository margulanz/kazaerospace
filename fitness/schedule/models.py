from django.db import models
from django.core.exceptions import ValidationError
from trainer.models import Trainer, Client

TIMESLOT_LIST = (
    ('09:00 – 10:00', '09:00 – 10:00'),
    ('10:00 – 11:00', '10:00 – 11:00'),
    ('11:00 – 12:00', '11:00 – 12:00'),
    ('12:00 – 13:00', '12:00 – 13:00'),
    ('13:00 – 14:00', '13:00 – 14:00'),
    ('14:00 – 15:00', '14:00 – 15:00'),
    ('15:00 – 16:00', '15:00 – 16:00'),
    ('16:00 – 17:00', '16:00 – 17:00'),
    ('17:00 – 18:00', '17:00 – 18:00')
)
DAYS_OF_WEEK = (
    (0, 'Понедельник'),
    (1, 'Вторник'),
    (2, 'Среда'),
    (3, 'Четверг'),
    (4, 'Пятница'),
    (5, 'Суббота'),
    (6, 'Воскресенье'),
)
ROOM_LIST = (
    (1, 'Зал 1'),
    (2, 'Зал 2'),
    (3, 'Зал 3'),
)


class AvailableTimeSlot(models.Model):
    timeslot = models.CharField(max_length=100, choices=TIMESLOT_LIST)
    weekday = models.IntegerField(choices=DAYS_OF_WEEK)
    room = models.IntegerField(choices=ROOM_LIST, null=True)

    class Meta:
        unique_together = ('timeslot', 'weekday', 'room')

    def __str__(self):
        weekday_name = dict(DAYS_OF_WEEK)[self.weekday]
        return f"{weekday_name} at {self.timeslot} in  Room {self.room}"


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    available_timeslots = models.ManyToManyField(AvailableTimeSlot)

    def __str__(self):
        return f"Расписание для {self.trainer}"


class Appointment(models.Model):
    timeslot = models.CharField(max_length=100, choices=TIMESLOT_LIST)
    date = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.IntegerField(choices=ROOM_LIST, null=True)

    class Meta:
        unique_together = (
            ('trainer', 'date', 'timeslot', 'room'),

            ('date', 'timeslot', 'client'),

            ('date', 'timeslot', 'trainer')

        )

    def clean(self):
        schedule = Schedule.objects.get(trainer=self.trainer)
        appointment = AvailableTimeSlot.objects.get(
            timeslot=self.timeslot, room=self.room, weekday=self.date.weekday())
        if not appointment in schedule.available_timeslots.all():
            raise ValidationError('Тренер не работает в это время')

    def __str__(self):
        return f"К тренеру {self.trainer.user.first_name} {self.trainer.user.last_name} записан {self.client} в {self.timeslot} на {self.date} в зале {self.room}"
