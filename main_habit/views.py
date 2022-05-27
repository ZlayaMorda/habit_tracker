from django.shortcuts import render
from django.http import HttpResponse

from main_habit.models import *

menu = [
    {'title': "Профиль", 'url_name': 'profile'},
    {'title': "Подборки", 'url_name': 'sets'},
    {'title': "Личные задачи", 'url_name': 'own_tasks'},
    {'title': "Войти", 'url_name': 'login'}
]


def main_page(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'main_habit/base.html', context=context)


def habit_sets(request):
    all_sets = HabitSet.objects.all()
    context = {
        'menu': menu,
        'title': 'Подборки',
        'all_sets': all_sets

    }
    return render(request, 'main_habit/sets.html', context=context)


def profile(request):
    return HttpResponse("Profile")


def own_tasks(request):
    return HttpResponse("Own_tasks")


def login(request):
    return HttpResponse("Login")
