"""
Tests with Django Dry Tests TestCase
"""
from django.test import tag
from dry_tests import (
    Request,
    TrueResponse as Response,
    SimpleTestCase,
    POST,
    Url,
)
# from .db_test_data import create_simple
# from demo.models import Simple


@tag('dry')
class ViewTestCase(SimpleTestCase):
    """
    Concrete TestCase inherited from DRY SimpleTestCase
    """

    def test_many(self):
        """
        Try check many pairs
        :return:
        """
        response_pairs = [
        (
            Request(url='/').get_url_response(self.client),
            Response(

                status_code=200,
            ),
        ),
        ]
        self.assertResponsesAreTrue(response_pairs)

    def test_main(self):
        """
        All asserts tests in one test function
        :return:
        """
        data = [
            # Multy parameters GET
            # DONE
            {
                'request': Request(url='/'),
                'response': Response(
                    status_code=200,
                    in_context='title',
                    context_values={'title': 'Title'},
                    content_values=['Title'],
                ),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            # Multy parameters POST
            {
                'request': Request(url='/', method=POST),
                'response': Response(
                    status_code=302,
                    redirect_url='/',
                ),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            # Failed assert
            {
                'request': Request(url='/'),
                'response': Response(content_values=['Error value']),
                'should_fail': True,
                'assert': self.assertTrueResponse,
            },
            # url_args
            {
                'request': Request(
                    url=Url(
                        url='/query/',
                        args=['kwarg_value']
                    )
                ),
                'response': Response(
                    context_values={'kwarg': 'kwarg_value'}
                ),
                'should_fail': False,
                'assert': self.assertContextValues,
            },
            # url_params
            {
                'request': Request(
                    url = Url(
                        url='/query/',
                        args=['kwarg_value'],
                        params={
                            'a': 'x',
                            'b': 'y',
                        }
                    )
                ),
                'response': Response(
                    context_values={
                        'kwarg': 'kwarg_value',
                        'a': 'x',
                        'b': 'y',
                    }
                ),
                'should_fail': False,
                'assert': self.assertContextValues,
            }
        ]

        for item in data:
            request = item['request']
            tru_response = request.get_url_response(self.client)
            expected_response = item['response']
            assert_function = item['assert']
            with self.subTest(msg=str(item)):
                if item['should_fail']:
                    with self.assertRaises(AssertionError):
                        assert_function(tru_response, expected_response)
                else:
                    assert_function(tru_response, expected_response)
