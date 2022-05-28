from rest_framework import serializers
from main_habit.models import *


class HabitSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitSet
        fields = ("habit_topic", )


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("name", "describe", "habit_set")


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ("time", "is_done", "habit")


class AchieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achieve
        fields = ("image", "statistics")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "achieves", "habit_sets", "avatar")
