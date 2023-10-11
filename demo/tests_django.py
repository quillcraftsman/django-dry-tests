"""
Tests with django TestCase
"""
from django.test import TestCase


class ViewTestCase(TestCase):

    def setUp(self):
        self.url = '/'

    def test_status_code_get(self):
        self.assertEqual(self.client.get(self.url).status_code, 200)

    def test_status_code_post(self):
        self.assertEqual(self.client.post(self.url).status_code, 302)

    def test_redirect_url(self):
        self.assertRedirects(self.client.post(self.url), '/')

    def test_value_in_context(self):
        self.assertIn('title', self.client.get(self.url).context)

    def test_context_value(self):
        self.assertEqual('Title', self.client.get(self.url).context['title'])

    def test_value_in_content(self):
        self.assertContains(self.client.get(self.url), 'Title', 1)
