from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from login_registration.forms import RegisterUserForm, LoginUserForm


def login(request):
    return render(request, 'login_registration/login.html', {'title': "Вход"})


def registration(request):
    return render(request, 'login_registration/registration.html', {'title': "Регистрация"})


class RegistrationUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'login_registration/registration.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login_registration/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
