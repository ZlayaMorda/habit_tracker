from urllib import request
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from main_habit.models import *
from .factories import *


class HabitListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_habits = 10
        for num in range(number_of_habits):
            HabitsFactory.create()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('sets'))
        self.assertEqual(resp.status_code, 302)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('sets'))
        self.assertEqual(resp.status_code, 302)

        self.assertTemplateUsed(resp, 'main_habit/sets.html')
