from django.shortcuts import render
from django.http import HttpResponse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def main_page(request):
    return render(request, 'main_habit/index.html', {'menu': menu, 'title': 'Главная страница'})
