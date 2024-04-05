from django.db.models.signals import post_save
from django.dispatch import receiver
from schedule.models import Schedule
from .models import User, Trainer, Client


@receiver(post_save, sender=User)
def create_trainer_or_client(sender, instance, created, **kwargs):
    if created:
        if instance.is_trainer:
            trainer = Trainer.objects.create(user=instance)
            Schedule.objects.create(trainer=trainer)
        else:
            Client.objects.create(user=instance)
