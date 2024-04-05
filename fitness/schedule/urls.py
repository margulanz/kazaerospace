from django.urls import include, path
from .views import GetTrainerSchedule, GetAppointment


urlpatterns = [
    path("<int:trainer_id>/", GetTrainerSchedule.as_view(),
         name='get_trainer_schedule'),
    path("<int:trainer_id>/appointments/",
         GetAppointment.as_view(), name='appointments')
]
