# Installation

1) `git clone https://github.com/margulanz/kazaerospace.git`
2) `cd kazaerospace`
3) `docker compose up --build`
4) Откройте Docker Desktop и зайдите в терминал контейнера `kazaerospace-backend-1`
5) `cd backend`
6) `python manage.py createsuperuser` для создания админ аккаунта
7) В браузере откройте http://localhost:8000/admin/ и войдите в админку


# Функционал
1) Заполните данные и поставте галочку если создаете тренера
![image](https://github.com/margulanz/kazaerospace/assets/37156990/13b58b31-aabe-4015-8da9-142d73826632) 
2) В зависимости от того поставили ли вы галочку, у Тренера или Клиента появится профиль где можно будет заполнить дополнительную информацию

![image](https://github.com/margulanz/kazaerospace/assets/37156990/8fa60970-adf0-4ed6-9fd6-5a3bb51b6060)

3) В Schedules вы можете сосавить расписания тренера, то есть по какому графику он работает в течении недели
4) В Appointment вы можете записать клиента к тренеру


# API
- `/schedule/<trainer_id>/` (GET) - получить расписание тренера
- `/schedule/<trainer_id>/appointments/` (GET) - получить информацию о записях к тренеру
