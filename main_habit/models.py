from datetime import date
from django.db import models


class Statistics(models.Model):
    time = models.DateField(default=date.today)
    Check = models.BooleanField(default=False)


class Achieve(models.Model):
    image = models.ImageField()
    statistics = models.AutoField()


class Habit(models.Model):
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=100)


class HabitSet(models.Model):
    habit_topic = models.CharField(max_length=30)
    habit_list = models.ManyToManyField(Habit)


class User(models.Model):
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    achieves = models.ManyToManyField(Achieve)
    habit_sets = models.ManyToManyField(HabitSet)
    avatar = models.ImageField()
