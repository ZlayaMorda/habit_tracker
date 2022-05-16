from django.contrib import admin
from django.urls import path

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('habits_collections/', include('habits_collections.urls')),
]
    
