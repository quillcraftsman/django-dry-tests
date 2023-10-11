"""
Base testcases
"""
from django.test import (
    # TestCase as DjangoTestCase,
    SimpleTestCase as DjangoSimpleTestCase,
)


class SimpleTestCase(DjangoSimpleTestCase):
    """
    Main TestCase without test database
    """

    def assertStatusCode(self, true_response, response):
        """
        Check status code
        :param request: Request
        :param response: Response
        :return: None
        """
        self.assertEqual(true_response.status_code, response.status_code)

    def assertRedirectUrl(self, true_response, response):
        """
        Check Redirect Url
        :param request: Request
        :param response: Response
        :return: None
        """
        self.assertRedirects(true_response, response.redirect_url)

    def assertValueInContext(self, true_response, response):
        """
        Check Value In Context
        :param request: Request
        :param response: Response
        :return: None
        """
        self.assertIn(response.in_context, true_response.context)

    def assertContextValues(self, true_response, response):
        """
        Check Context Value
        :param request: Request
        :param response: Response
        :return: None
        """
        context = true_response.context
        context_values = response.context_values
        for key, value in context_values.items():
            self.assertIn(key, context)
            self.assertEqual(value, context[key])

    def assertContentValues(self, true_response, response):
        """
        Check Content Value
        :param request: Request
        :param response: Response
        :return: None
        """
        for content_value in response.get_content_values():
            self.assertContains(true_response, content_value.value, content_value.count)

    def assertDRY(self, true_response, response):
        """
        Main assert for request and response
        Check all parameters sent in response
        :param request: Request
        :param response: Response
        :return: None
        """
        if response.status_code:
            self.assertStatusCode(true_response, response)
        if response.redirect_url:
            self.assertRedirectUrl(true_response, response)
        if response.in_context:
            self.assertValueInContext(true_response, response)
        if response.context_values:
            self.assertContextValues(true_response, response)
        if response.content_values:
            self.assertContentValues(true_response, response)

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
