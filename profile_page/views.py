from django.shortcuts import render
from main_habit.some_info import *


def profile(request):
    context = {
            'menu': menu,
            'title': 'Профиль',
        }
    return render(request, 'profile_page/profile.html', context=context)