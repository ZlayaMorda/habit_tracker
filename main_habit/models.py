from datetime import date

from django.contrib.auth.models import User
from django.db import models


class HabitSet(models.Model):
    habit_topic = models.CharField(max_length=62)

    def __str__(self):
        return self.habit_topic


class Habit(models.Model):
    name = models.CharField(max_length=62)
    describe = models.CharField(max_length=126)
    habit_set = models.ForeignKey(HabitSet, related_name='habits', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Statistics(models.Model):
    time = models.DateField(default=date.today)
    is_done = models.BooleanField(default=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)


class Achieve(models.Model):
    image = models.ImageField()
    statistics = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    achieves = models.ManyToManyField(Achieve)
    habit_sets = models.ManyToManyField(HabitSet)
    avatar = models.ImageField()
