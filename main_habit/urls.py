from django.urls import path
from .views import *
from profile_page.views import profile

urlpatterns = [
    path('', main_page, name='main'),
    path('sets/', HabitSetList.as_view(), name='sets'),
    path('profile/', profile, name='profile'),
    path('own_tasks/', own_tasks, name='own_tasks'),
    path('login/', login, name='login')
]
