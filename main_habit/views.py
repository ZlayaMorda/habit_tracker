from django.shortcuts import render
from django.http import HttpResponse

menu = ["Профиль", "Подборки", "Обратная связь", "Войти"]


def main_page(request):
    return render(request, 'main_habit/base.html', {'menu': menu, 'title': 'Главная страница'})
