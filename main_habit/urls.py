from django.urls import path

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
    path('own_tasks/', UserHabitSetList.as_view(), name='own_tasks'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('register/', RegistrationUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('sets/<int:set_id>', add_set_to_user, name='add_set'),
    path('own_tasks/set_habit_check/', set_habit_check, name='set_habit_check')
]
