"""
Tests with Django Dry Tests TestCase
"""
from django.test import tag
from dry_tests import (
    Request,
    TrueResponse as Response,
    SimpleTestCase,
    TestCase,
    POST,
    Url,
    Context,
)
# from .db_test_data import create_simple
# from demo.models import Simple


class AssertTrueMixin:
    """
    Mixin for Simple test case and TestCase
    """
    def setUp(self):
        """
        Setup test data
        :return:
        """
        self.url = '/'
        self.request = Request(url=self.url)
        self.true_response = Response(
            status_code=200,
            context=Context(
                keys=['title'],
                items={'title': 'Title'},
                values=['Title'],
                types={'title': str},
            ),
            content_values=['Title'],
        )

    def testAssertTrueResponse(self):
        """
        True test get method
        :return:
        """
        # GET
        current_response = self.request.get_response(self.client)
        self.assertTrueResponse(current_response, self.true_response)

    def testContextAsDict(self):
        """
        Test send context as dict
        :return:
        """
        request = Request(
            url=self.url
        )
        true_response = Response(
            context={
                'title': 'Title'
            }
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def testAssertTrueResponsePost(self):
        """
        True test Post method
        :return:
        """
        request = Request(url='/', method=POST)
        true_response = Response(
            status_code=302,
            redirect_url='/',
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

        # With Url as redirect url
        request = Request(url='/', method=POST)
        true_response = Response(
            redirect_url=Url(
                url='/'
            ),
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def testAssertResponsesAreTrue(self):
        """
        Test Many responses
        :return:
        """
        responses = [
            (
                self.request.get_response(self.client),
                self.true_response,
             )
        ]
        self.assertResponsesAreTrue(responses)

    def testArgs(self):
        """
        Test url with args
        :return:
        """
        request = Request(
            url=Url(
                url='/query/',
                args=['kwarg_value']
            )
        )
        true_response = Response(
            context = Context(
                items={'kwarg': 'kwarg_value'}
            )
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def testParams(self):
        """
        Test Url with params
        :return:
        """
        request = Request(
            url = Url(
                url='/query/',
                args=['kwarg_value'],
                params={
                    'a': 'x',
                    'b': 'y',
                }
            )
        )
        true_response = Response(
            context=Context(
                items={
                    'kwarg': 'kwarg_value',
                    'a': 'x',
                    'b': 'y',
                }
            )
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


@tag('dry')
class AssertTrueTestCase(AssertTrueMixin, TestCase):
    """
        Concrete TestCase inherited from DRY TestCase (with db)
        All asserts Should not fail
        """

@tag('dry')
class AssertTrueSimpleTestCase(AssertTrueMixin, SimpleTestCase):
    """
    Concrete TestCase inherited from DRY SimpleTestCase
    All asserts Should not fail
    """


@tag('dry')
class AssertFalseSimpleTestCase(SimpleTestCase):
    """
    Concrete TestCase inherited from DRY SimpleTestCase
    All asserts should fail
    """

    def test_failed(self):
        """
        All asserts should fail
        :return:
        """
        error_responses = []

        status_code = 404

        error_responses.append(
            Response(
                status_code=status_code
            )
        )

        contexts = [
            Context(
                keys=['error key']
            ),
            Context(
                items={'title': 'Error item'}
            ),
            Context(
                items={'error key': 'Title'}
            ),
            Context(
                values=['Error value']
            ),
            Context(
                types={'title': list}
            )
        ]

        for context in contexts:
            error_responses.append(
                Response(context=context)
            )

        content_values = ['Error value']

        error_responses.append(
            Response(
                content_values=content_values
            )
        )

        for error_response in error_responses:
            request = Request(
                url='/'
            )
            current_response = request.get_response(self.client)
            with self.subTest(msg=str(error_response)):
                with self.assertRaises(AssertionError):
                    self.assertTrueResponse(current_response, error_response)
