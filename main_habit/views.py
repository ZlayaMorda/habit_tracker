from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.views import APIView

from main_habit.serializers import *
from main_habit.some_info import *


def main_page(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'main_habit/base.html', context=context)


class HabitSetList(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_habit/sets.html'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        queryset = HabitSet.objects.filter(~Q(profile__user=request.user))
        return Response({'all_sets': queryset, 'title': 'Подборки', 'menu': menu})


class UserHabitSetList(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_habit/user_sets.html'
    redirect_field_name = 'redirect_to'
    day_now = date.today()

    def get(self, request):
        queryset = request.user.profile.habit_sets.all()
        for q in queryset:
            for h in q.habits.all():
                Statistics.objects.get_or_create(time=self.day_now, habit=h, profile=request.user.profile)
        statistics_set = Statistics.objects.filter(time=self.day_now)
        return Response({'all_sets': queryset, 'title': 'Подборки', 'menu': menu, 'statistics_set': statistics_set})


def logout_user(request):
    logout(request)
    return redirect('login')
# @api_view(['GET'])
# def habit_set_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         sets = HabitSet.objects.all()
#         serializer = HabitSetSerializer(sets, many=True)
#         return Response(serializer.data)
#
#
# def habit_sets(request):
#     # all_sets = HabitSet.objects.all()
#     all_sets = habit_set_list(request)
#     context = {
#         'menu': menu,
#         'title': 'Подборки',
#         'all_sets': all_sets
#
#     }
#     return render(request, 'main_habit/sets.html', context=context)


def add_set_to_user(request, set_id):
    # if True:
    #     user = request.user
    #     prof = Profile(user)
    #     user.profile = prof
    #     user.profile.save()
    add_set = HabitSet.objects.get(pk=set_id)
    # Profile.objects.get_or_create(user=request.user)
    request.user.profile.habit_sets.add(add_set)
    return redirect('sets')


@login_required
def own_tasks(request):
    return HttpResponse("Own_tasks")
