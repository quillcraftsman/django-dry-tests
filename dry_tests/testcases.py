from django.test import TestCase as DjangoTestCase
from .models import GET, POST


class TestCase(DjangoTestCase):

    def get_url_response(self, request):
        requests = {
            GET: self.client.get,
            POST: self.client.post
        }

        url_response = requests[request.method](request.url)
        return url_response

    def assertStatusCode(self, request, response):
        url_response = self.get_url_response(request)
        self.assertEqual(url_response.status_code, response.status_code)

    def assertRedirectUrl(self, request, response):
        url_response = self.get_url_response(request)
        self.assertRedirects(url_response, response.redirect_url)

    def assertValueInContext(self, request, response):
        url_response = self.get_url_response(request)
        self.assertIn(response.in_context, url_response.context)

    def assertContextValues(self, request, response):
        url_response = self.get_url_response(request)
        context = url_response.context
        context_values = response.context_values
        for key, value in context_values.items():
            self.assertIn(key, context)
            self.assertEqual(value, context[key])

    def assertContentValue(self, request, response):
        # TODO: Response send every time - it's not good
        url_response = self.get_url_response(request)
        self.assertContains(url_response, response.content_value)
