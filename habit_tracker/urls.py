from django.contrib import admin
from django.urls import path

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_habit.urls')),
    path('', include('login_registration.urls')),
    path('', include('profile_page.urls'))
]

