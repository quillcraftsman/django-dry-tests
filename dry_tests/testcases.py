"""
Base testcases
"""
from django.test import TestCase as DjangoTestCase
from .models import GET, POST


class TestCase(DjangoTestCase):
    """
    Main TestCase with test database
    """

    def get_url_response(self, request):
        """
        get response with test client
        :param request: Request model
        :return: client response
        """
        requests = {
            GET: self.client.get,
            POST: self.client.post
        }

        # if request.data is None:
        #     url_response = requests[request.method](request.url)
        # else:
        url_response = requests[request.method](request.url, data=request.data)

        return url_response

    def assertStatusCode(self, request, response):
        """
        Check status code
        :param request: Request
        :param response: Response
        :return: None
        """
        url_response = self.get_url_response(request)
        self.assertEqual(url_response.status_code, response.status_code)

    def assertRedirectUrl(self, request, response):
        """
        Check Redirect Url
        :param request: Request
        :param response: Response
        :return: None
        """
        url_response = self.get_url_response(request)
        self.assertRedirects(url_response, response.redirect_url)

    def assertValueInContext(self, request, response):
        """
        Check Value In Context
        :param request: Request
        :param response: Response
        :return: None
        """
        url_response = self.get_url_response(request)
        self.assertIn(response.in_context, url_response.context)

    def assertContextValues(self, request, response):
        """
        Check Context Value
        :param request: Request
        :param response: Response
        :return: None
        """
        url_response = self.get_url_response(request)
        context = url_response.context
        context_values = response.context_values
        for key, value in context_values.items():
            self.assertIn(key, context)
            self.assertEqual(value, context[key])

    def assertContentValue(self, request, response):
        """
        Check Content Value
        :param request: Request
        :param response: Response
        :return: None
        """
        # TODO: Response send every time - it's not good
        url_response = self.get_url_response(request)
        self.assertContains(url_response, response.content_value)

    def assertCreated(self, request, response):
        """
        Check object was created
        :param request: Request
        :param response: Response
        :return: None
        """
        created = response.created
        model = created['model']
        fields = created['fields']
        self.assertFalse(model.objects.filter(**fields).exists())
        self.get_url_response(request)
        self.assertTrue(model.objects.filter(**fields).exists())
