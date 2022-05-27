from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('sets/', habit_sets, name='sets'),
    path('profile/', profile, name='profile'),
    path('own_tasks/', own_tasks, name='own_tasks'),
    path('login/', login, name='login')
]
