from django.urls import path

from profile_page.views import *

urlpatterns = [
    path('profile/', ProfileInfo.as_view(), name='profile'),
]
