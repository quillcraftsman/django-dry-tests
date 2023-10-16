"""
URL configuration for settings project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo.urls')),
    path('quickstart/', include('quickstart.urls')),
]
