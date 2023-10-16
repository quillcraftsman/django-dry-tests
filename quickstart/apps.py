"""
App module for quickstart App
"""
from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    """
    Config class for quickstart app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickstart'
