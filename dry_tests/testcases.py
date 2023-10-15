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
        self.assertRedirects(current_response, true_response.get_redirect_url())

    def assertKeysInContext(self, current_response, true_response):
        """
        Check Value In Context
        :param request: Request
        :param response: Response
        :return: None
        """
        for key in true_response.get_context().keys:
            self.assertIn(key, current_response.context)

    def assertValuesInContext(self, current_response, true_response):
        """
        Check Value In Context
        :param request: Request
        :param response: Response
        :return: None
        """
        # .flatten() - make dict from request context
        current_response_context_values = current_response.context.flatten().values()
        for value in true_response.context.values:
            self.assertIn(value, current_response_context_values)

    def assertContextItems(self, current_response, true_response):
        """
        Check Context Value
        :param current_response: HttpResponse
        :param true_response: TrueResponse
        :return: None
        """
        context = current_response.context
        context_items = true_response.get_context().items
        for key, value in context_items.items():
            self.assertIn(key, context)
            self.assertEqual(value, context[key])

    def assertContextTypes(self, current_response, true_response):
        """
        Check context values types
        :param current_response: HttpResponse
        :param true_response: TrueResponse
        :return:
        """
        context = current_response.context
        context_types = true_response.get_context().types
        for key, value in context_types.items():
            self.assertIn(key, context)
            self.assertTrue(isinstance(context[key], value))

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
            # Not ?
        # context
        true_response_context = true_response.get_context()
        if true_response_context:
            if true_response_context.keys:
                self.assertKeysInContext(current_response, true_response)
            if true_response_context.items:
                self.assertContextItems(current_response, true_response)
            if true_response_context.values:
                self.assertValuesInContext(current_response, true_response)
            if true_response_context.types:
                self.assertContextTypes(current_response, true_response)
        if true_response.content_values:
            self.assertContentValues(current_response, true_response)

    def assertFormFieldsCount(self, current_form, true_form):
        """
        Check fields count
        :param current_form:
        :param true_form:
        :return:
        """
        self.assertEqual(len(current_form.fields), true_form.fields.count)

    def assertFieldsInForm(self, current_form, true_form):
        """
        Check fields in form
        :param current_form:
        :param true_form:
        :return:
        """
        for name in true_form.fields.names:
            self.assertIn(name, current_form.fields)

    def assertFormTypes(self, current_form, true_form):
        """
        Check form fields types
        :param current_form:
        :param true_form:
        :return:
        """
        for name, form_type in true_form.fields.types.items():
            fields = current_form.fields
            self.assertIn(name, fields)
            self.assertIsInstance(fields[name], form_type)


    def assertTrueForm(self, current_form, true_form):
        """
        Main assert for Forms
        :param current_form: django form
        :param true_form: TrueForm
        :return: None
        """
        fields = true_form.fields
        if fields:
            if fields.count:
                self.assertFormFieldsCount(current_form, true_form)
            if fields.names:
                self.assertFieldsInForm(current_form, true_form)
            if fields.types:
                self.assertFormTypes(current_form, true_form)

    def assertResponsesAreTrue(self, response_pairs):
        """
        Check all response pairs
        :param response_pairs:
        :return:
        """
        for current_response, true_response in response_pairs:
            self.assertTrueResponse(current_response, true_response)

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
