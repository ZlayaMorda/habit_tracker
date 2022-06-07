from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from habit_tracker.settings import dev
from .models import *
import datetime


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    # movies = Movie.objects.filter(draft=False, date_creation__gte=date_from)
    mail_subject = "habits"
    for user in users:
        to_email = user.email
        true_habits = Statistics.objects.filter(time=date.today() - datetime.timedelta(days=1), profile__user=user, is_done=True).count()
        message = f"Вчера ты выполнил задач: {true_habits}. Не будь тряпкой и сделай сегодня больше!"
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=dev.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return "Done"
