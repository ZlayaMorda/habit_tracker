import json
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from main_habit.models import *
from main_habit.some_info import *


@login_required
def profile(request):
    context = {
        'menu': menu,
        'title': 'Профиль',
    }
    return render(request, 'profile_page/profile.html', context=context)


class ProfileInfo(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_page/profile.html'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        username = request.user.username
        table_true = []
        table_false = []
        for i in range(6, -1, -1):
            table_true.append([str(date.today() - timedelta(days=i)),
                               Statistics.objects.filter(profile__user=request.user, time=date.today() - timedelta(days=i), is_done=True).count()])
            table_false.append([str(date.today() - timedelta(days=i)),
                                Statistics.objects.filter(profile__user=request.user, time=date.today() - timedelta(days=i),
                                                          is_done=False).count()])

        table_true_str = json.dumps(table_true)
        table_false_str = json.dumps(table_false)

        habits_name = Habits.objects.filter(habit_set__profile=request.user.profile)
        habit_dict = {}
        for i in habits_name:
            all_habits = Statistics.objects.filter(profile__user=request.user, habit=i).count()
            true_habits = Statistics.objects.filter(profile__user=request.user, is_done=True, habit=i).count()
            habit_dict[i.name] = (all_habits, true_habits, int(true_habits/all_habits * 100))

        return Response({'username': username, 'title': 'Профиль', 'menu': menu,
                         'table_true': table_true_str, 'table_false': table_false_str,
                         'habits_dict': habit_dict}, )
