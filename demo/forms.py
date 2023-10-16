"""
Demo forms module
"""
from django import forms


class DemoForm(forms.Form):
    """
    Demo form class
    """
    name = forms.CharField(max_length=5)
    number = forms.IntegerField(initial=3)
