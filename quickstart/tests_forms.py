"""
Tests Forms with Django Dry Tests TestCase
"""
from django.test import tag
from django import forms
from quickstart.forms import ExampleForm
from dry_tests import (
    SimpleTestCase,
)
from dry_tests.models import TrueForm, Fields


@tag('dry')
class ExampleFromTestCase(SimpleTestCase):
    """
    Example Form Test Class
    """

    def test_form(self):
        """
        Example Test with django-dry-tests
        :return:
        """
        true_form = TrueForm(  # Set Up TrueForm instance
               Fields(  # TrueForm Fields
                   count=2,  # check fields count
                   names=[
                       'number', 'name'
                   ],  # check field names
                   types={
                       'name': forms.CharField,
                       'number': forms.IntegerField
                   }  # check fields types
               ),
            )
        current_form = ExampleForm()  # Get project form
        self.assertTrueForm(current_form, true_form)  # use this main assert to check all conditions
