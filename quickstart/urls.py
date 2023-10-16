"""
URL configuration for settings project.
"""
from django.urls import path
from . import views

app_name = 'quickstart'

urlpatterns = [
    path('', views.quickstart_view, name='quickstart'),
]
