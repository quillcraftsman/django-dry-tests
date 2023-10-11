"""
Tests with django TestCase
"""
from django.test import TestCase, SimpleTestCase
from demo.models import Simple


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


class ViewTestCase(TestCase):
    """
    Django tests with database
    """

    def setUp(self):
        """
        Set Up test data
        :return:
        """
        self.url = '/'

    def test_new_object_created(self):
        """
        Test New Object Was Created
        :return:
        """
        data = {
            'name': 'new_name'
        }
        self.assertFalse(Simple.objects.filter(name='new_name').exists())
        self.client.post(self.url, data=data)
        self.assertTrue(Simple.objects.filter(name='new_name').exists())

    # def test_object_updated(self):
    #     first = Simple.objects.create(name='first')
    #     url = f'/{first.pk}/'
    #     data = {
    #         'name': 'updated_name'
    #     }
    #     self.assertTrue(Simple.objects.filter(name='first').exists())
    #     self.client.post(url, data=data)
    #     self.assertTrue(Simple.objects.filter(name='updated_name').exists())

    def test_detail_view(self):
        """
        Test Detail View
        :return:
        """
        first = Simple.objects.create(name='first')
        url = f'/{first.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
