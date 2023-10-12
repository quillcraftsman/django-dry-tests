"""
URL configuration for settings project.
"""
from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index_view),
    path('<int:pk>/', views.one_view),
    path('query/<str:kwarg>/', views.param_view),
]
