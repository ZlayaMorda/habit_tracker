from django.urls import path

from main_habit.views import main_page
from .views import *


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegistrationUser.as_view(), name='register')
]
