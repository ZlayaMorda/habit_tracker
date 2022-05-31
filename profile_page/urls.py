from django.urls import path

from login_registration.views import LoginUser
from .views import *
from main_habit.views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('sets/', HabitSetList.as_view(), name='sets'),
    path('profile/', profile, name='profile'),
    path('own_tasks/', own_tasks, name='own_tasks'),
    path('login/', LoginUser.as_view(), name='login')
]
