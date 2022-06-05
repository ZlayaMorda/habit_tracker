from unittest import TestCase
from .factories import *


class TestHabitSet(TestCase):

    @classmethod
    def setUpTestData(cls):
        HabitSetFactory.create()

    def test_str(self):
        sets = HabitSet.objects.get(id=1)
        expected_set = sets.habit_topic
        self.assertEqual(str(sets), expected_set)


class TestHabits(TestCase):

    @classmethod
    def setUpTestData(cls):
        HabitsFactory.create()

    def test_foreign_str(self):
        habit_set = HabitSet.objects.get(id=1)
        habit = habit_set.habits.get(id=1)
        just_habit = Habits.objects.get(id=1)
        self.assertEqual(habit, just_habit)
