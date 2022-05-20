from django.urls import path
from .views import *

urlpatterns = [
    path('', habits_list, name='habits'),
]
