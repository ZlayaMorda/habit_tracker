from django.urls import path

from main_habit.views import main_page
from .views import *


urlpatterns = [
    path('', main_page, name='main'),
    path('login/', login, name='login'),
    path('register/', registration, name='register')
]
