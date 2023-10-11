"""
DRY Tests django app
"""
from django.apps import AppConfig


class DryTestsConfig(AppConfig):
    """
    Dry Tests App Config Class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dry_tests'
