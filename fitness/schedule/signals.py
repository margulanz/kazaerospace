from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AvailableTimeSlot, TIMESLOT_LIST, DAYS_OF_WEEK, ROOM_LIST


@receiver(post_migrate)
def create_timeslots(sender, **kwargs):
    for weekday in DAYS_OF_WEEK:
        for timeslot in TIMESLOT_LIST:
            for room in ROOM_LIST:
                AvailableTimeSlot.objects.get_or_create(
                    weekday=weekday[0], timeslot=timeslot[1], room=room[0])
