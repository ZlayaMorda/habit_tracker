from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class HabitSet(models.Model):
    habit_topic = models.CharField(max_length=62)

    def __str__(self):
        return self.habit_topic


class Habits(models.Model):
    name = models.CharField(max_length=62)
    describe = models.CharField(max_length=126)
    habit_set = models.ForeignKey(HabitSet, related_name='habits', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Statistics(models.Model):
    time = models.DateField(default=date.today)
    is_done = models.BooleanField(default=False)
    habit = models.ForeignKey(Habits, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'statistics'


class Achieve(models.Model):
    image = models.ImageField()
    statistics = models.IntegerField()

    def __str__(self):
        return 'achieve'


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    achieves = models.ManyToManyField(Achieve)
    habit_sets = models.ManyToManyField(HabitSet)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.get_username()


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
