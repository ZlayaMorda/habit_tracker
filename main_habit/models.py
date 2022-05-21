from datetime import date
from django.db import models


class HabitSet(models.Model):
    habit_topic = models.CharField(max_length=62)


class Habit(models.Model):
    name = models.CharField(max_length=62)
    describe = models.CharField(max_length=126)
    habit_set = models.ForeignKey(HabitSet, on_delete=models.CASCADE)


class Statistics(models.Model):
    time = models.DateField(default=date.today)
    is_done = models.BooleanField(default=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)


class Achieve(models.Model):
    image = models.ImageField()
    statistics = models.IntegerField()


class User(models.Model):
    nickname = models.CharField(max_length=62)
    email = models.EmailField()
    password = models.CharField(max_length=62)
    achieves = models.ManyToManyField(Achieve)
    habit_sets = models.ManyToManyField(HabitSet)
    avatar = models.ImageField()
