from django.shortcuts import render


def login(request):
    return render(request, 'login_registration/login.html', {'title': "Вход"})


def registration(request):
    return render(request, 'login_registration/registration.html', {'title': "Регистрация"})
