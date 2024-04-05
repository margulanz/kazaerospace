from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

sex_choices = (
    ('Муж', 'Мужчина'),
    ('Жен', 'Женщина')
)


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=sex_choices)
    is_trainer = models.BooleanField(default=False)


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField(default=0, null=True, blank=True)
    phone_number = PhoneNumberField(
        unique=True, default=None, null=True, blank=True)
    education = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Тренер)"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Клиент)"
