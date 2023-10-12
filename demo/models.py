"""
Demo models
"""
from django.db import models


class Simple(models.Model):
    """
    Simple model with unique name
    """
    name = models.CharField(max_length=32, unique=True)
