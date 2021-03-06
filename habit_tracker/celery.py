import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habit_tracker.settings.dev')

app = Celery('habit_tracker')

app.config_from_object('django.conf:settings.dev', namespace='CELERY')

app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-6': {
        'task': 'main_habit.tasks.send_mail_func',
        'schedule': crontab(hour=6, minute=0)
    }

}

app.autodiscover_tasks()
