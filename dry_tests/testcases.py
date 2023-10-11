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

    def assertStatusCode(self, current_response, true_response):
        """
        Check status code
        :param request: Request
        :param response: Response
        :return: None
        """
        self.assertEqual(current_response.status_code, true_response.status_code)

    def assertRedirectUrl(self, current_response, true_response):
        """
        Check Redirect Url
        :param request: Request
        :param response: Response
        :return: None
        """
        self.assertRedirects(current_response, true_response.redirect_url)

    def assertValueInContext(self, current_response, true_response):
        """
        Check Value In Context
        :param request: Request
        :param response: Response
        :return: None
        """
        self.assertIn(true_response.in_context, current_response.context)

    def assertContextValues(self, current_response, true_response):
        """
        Check Context Value
        :param request: Request
        :param response: Response
        :return: None
        """
        context = current_response.context
        context_values = true_response.context_values
        for key, value in context_values.items():
            self.assertIn(key, context)
            self.assertEqual(value, context[key])

    def assertContentValues(self, current_response, true_response):
        """
        Check Content Value
        :param request: Request
        :param response: Response
        :return: None
        """
        for content_value in true_response.get_content_values():
            self.assertContains(current_response, content_value.value, content_value.count)

    def assertTrueResponse(self, current_response, true_response):
        """
        Main assert for request and response
        Check all parameters sent in response
        :param request: Request
        :param response: Response
        :return: None
        """
        if true_response.status_code:
            self.assertStatusCode(current_response, true_response)
        if true_response.redirect_url:
            self.assertRedirectUrl(current_response, true_response)
        if true_response.in_context:
            self.assertValueInContext(current_response, true_response)
        if true_response.context_values:
            self.assertContextValues(current_response, true_response)
        if true_response.content_values:
            self.assertContentValues(current_response, true_response)

    def assertResponseIsTrue(self, response_pair):
        self.assertTrueResponse(response_pair.current_response, response_pair.true_response)

    def assertResponsesAreTrue(self, response_pairs):
        for response_pair in response_pairs:
            self.assertResponseIsTrue(response_pair)

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
