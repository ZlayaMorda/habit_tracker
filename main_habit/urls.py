from django.urls import path

from login_registration.views import login, registration
from .views import *
from profile_page.views import profile

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', main_page, name='main'),
    path('sets/', HabitSetList.as_view(), name='sets'),
    path('profile/', profile, name='profile'),
    path('own_tasks/', own_tasks, name='own_tasks'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', login, name='login'),
    path('register/', registration, name='register')
]
