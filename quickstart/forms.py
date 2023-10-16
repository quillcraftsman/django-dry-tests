"""
Example forms module
"""
from django import forms


class ExampleForm(forms.Form):
    """
    Example form class
    """
    name = forms.CharField(max_length=5)
    number = forms.IntegerField(initial=3)
