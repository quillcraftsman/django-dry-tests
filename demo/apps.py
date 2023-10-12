"""
Demo app module
"""
from django.apps import AppConfig


class DemoConfig(AppConfig):
    """
    Demo app config class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'
