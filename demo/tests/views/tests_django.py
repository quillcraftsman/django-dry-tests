"""
Tests with django TestCase
"""
from django.test import SimpleTestCase, tag
# from demo.models import Simple


@tag("django")
class ViewSimpleTestCase(SimpleTestCase):
    """
    Django Test Case to Test views without database
    """

    def setUp(self):
        """
        Set Up test data
        :return:
        """
        self.url = '/'

    def test_status_code_get(self):
        """
        Test get status code
        :return:
        """
        self.assertEqual(self.client.get(self.url).status_code, 200)

    def test_status_code_post(self):
        """
        Test post status code
        :return:
        """
        self.assertEqual(self.client.post(self.url).status_code, 302)

    def test_redirect_url(self):
        """
        Test Success Redirect
        :return:
        """
        self.assertRedirects(self.client.post(self.url), '/')

    def test_value_in_context(self):
        """
        Test Context Contains Value
        :return:
        """
        self.assertIn('title', self.client.get(self.url).context)

    def test_context_value(self):
        """
        Test Context Value
        :return:
        """
        self.assertEqual('Title', self.client.get(self.url).context['title'])

    def test_value_in_content(self):
        """
        Test Value in Content
        :return:
        """
        self.assertContains(self.client.get(self.url), 'Title', 1)

    def test_query_params_and_kwargs(self):
        """
        Send kwargs and query params to url
        :return:
        """
        url = '/query/kwarg_value/?a=x&b=y'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        context = response.context
        self.assertIn('a', context)
        self.assertIn('b', context)
        self.assertIn('kwarg', context)
        self.assertEqual(context['a'], 'x')
        self.assertEqual(context['b'], 'y')
        self.assertEqual(context['kwarg'], 'kwarg_value')
