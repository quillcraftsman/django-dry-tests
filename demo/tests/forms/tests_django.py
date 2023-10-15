"""
Tests with django TestCase
"""
from django.test import SimpleTestCase, tag
from django import forms
from demo.forms import DemoForm


@tag("django")
class FormTestCase(SimpleTestCase):
    """
    Django Test Case to Test views without database
    """
    def test_form(self):
        """
        Test form main features
        :return:
        """
        form = DemoForm()
        self.assertEqual(len(form.fields), 2)
        self.assertIn('name', form.fields)
        self.assertIn('number', form.fields)
        self.assertTrue(isinstance(form.fields['name'], forms.CharField))
        self.assertTrue(isinstance(form.fields['number'], forms.IntegerField))
