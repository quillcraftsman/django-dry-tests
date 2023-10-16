"""
Tests Forms with Django Dry Tests TestCase
"""
from django.test import tag
from django import forms
from demo.forms import DemoForm
from dry_tests import (
    SimpleTestCase
)
from dry_tests.models import TrueForm, Fields


@tag('dry')
class DemoFromTestCase(SimpleTestCase):
    """
    Demo Form Test Class
    """

    def test_form(self):
        """
        Main test for form
        :return:
        """
        true_forms = [
            TrueForm(
               Fields(
                   count=2,
                   names=[
                       'number', 'name'
                   ],
                   types={
                       'name': forms.CharField,
                       'number': forms.IntegerField
                   }
               ),
            )
        ]
        current_form = DemoForm()
        for true_form in true_forms:
            self.assertTrueForm(current_form, true_form)

    def test_form_failed(self):
        """
               Failed test for form
               :return:
               """
        fail_forms = [
            TrueForm(
                Fields(
                    count=3,
                )
            ),
            TrueForm(
                Fields(
                    names=['error_name']
                )
            ),
            TrueForm(
                Fields(
                    types={
                        'name': forms.IntegerField
                    }
                )
            )
        ]
        current_form = DemoForm()
        for fail_form in fail_forms:
            with self.assertRaises(AssertionError):
                self.assertTrueForm(current_form, fail_form)
