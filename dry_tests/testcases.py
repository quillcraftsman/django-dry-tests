"""
Base testcases
"""
from django.test import (
    # TestCase as DjangoTestCase,
    SimpleTestCase as DjangoSimpleTestCase,
)
from .models import GET, POST


class SimpleTestCase(DjangoSimpleTestCase):
    """
    Main TestCase with test database
    """

    @staticmethod
    def make_url(request):
        """
        Make url with params and kwargs
        :param request:
        :return:
        """
        url = request.url
        # url_args
        url_args_list = request.url_args
        if url_args_list:
            url_args = '/'.join(url_args_list)
            url = f'{url}{url_args}/'
        # url_params
        url_params_dict = request.url_params
        if url_params_dict:
            url_params_list = []
            for key, value in url_params_dict.items():
                pair = f'{key}={value}'
                url_params_list.append(pair)
            url_params_str = '&'.join(url_params_list)
            url = f'{url}?{url_params_str}'
        return url

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

        url = self.make_url(request)
        url_response = requests[request.method](url, data=request.data)

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

    def assertDRY(self, request, response):
        """
        Main assert for request and response
        Check all parameters sended in response
        :param request: Request
        :param response: Response
        :return: None
        """
        if response.status_code:
            self.assertStatusCode(request, response)
        if response.redirect_url:
            self.assertRedirectUrl(request, response)
        if response.in_context:
            self.assertValueInContext(request, response)
        if response.context_values:
            self.assertContextValues(request, response)
        if response.content_value:
            self.assertContentValue(request, response)

    # def assertCreated(self, request, response):
    #     """
    #     Check object was created
    #     :param request: Request
    #     :param response: Response
    #     :return: None
    #     """
    #     created = response.created
    #     model = created['model']
    #     fields = created['fields']
    #     self.assertFalse(model.objects.filter(**fields).exists())
    #     self.get_url_response(request)
    #     self.assertTrue(model.objects.filter(**fields).exists())
