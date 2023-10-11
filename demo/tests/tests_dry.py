"""
Tests with Django Dry Tests TestCase
"""
from dry_tests import (
    Request,
    TrueResponse as Response,
    SimpleTestCase,
    POST,
    Url,
    ContentValue,
    ResponsePair,
)
# from .db_test_data import create_simple
# from demo.models import Simple


class ViewTestCase(SimpleTestCase):
    """
    Concrete TestCase inherited from DRY SimpleTestCase
    """

    # def test_many(self):
    #     data = [
    #         {
    #             'request': Request(url='/').get_url_response(self.client),
    #             'response': Response(
    #                 status_code=200,
    #                 in_context='title',
    #                 context_values={'title': 'Title'},
    #                 content_values=['Title'],
    #             ),
    #         },
    #         # Multy parameters POST
    #         {
    #             'request': Request(url='/', method=POST).get_url_response(self.client),
    #             'response': Response(
    #                 status_code=302,
    #                 redirect_url='/',
    #             ),
    #         },
    #     ]
    #
    #     self.assertManyExpectedResponses(data)

    def test_response_pair(self):
        response_pair = ResponsePair(
                            current_response=Request(url='/').get_url_response(self.client),
                            true_response=Response(
                                status_code=200,
                                in_context='title',
                                context_values={'title': 'Title'},
                                content_values=['Title'],
                            ),
                        )
        self.assertResponseIsTrue(response_pair)

    def test_many_pairs(self):
        response_pairs = [
        ResponsePair(
            current_response=Request(url='/').get_url_response(self.client),
            true_response=Response(
                status_code=200,
                in_context='title',
                context_values={'title': 'Title'},
                content_values=['Title'],
            ),
        ),
        ResponsePair(
            current_response=Request(url='/').get_url_response(self.client),
            true_response=Response(
                status_code=200,
                in_context='title',
                context_values={'title': 'Title'},
                content_values=['Title'],
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
            # RedirectUrl
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=302, redirect_url='/'),
                'should_fail': False,
                'assert': self.assertRedirectUrl,
            },
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=302, redirect_url='/fail_redirect/'),
                'should_fail': True,
                'assert': self.assertRedirectUrl,
            },
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=302, redirect_url='/'),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=302, redirect_url='/fail_redirect/'),
                'should_fail': True,
                'assert': self.assertTrueResponse,
            },
            # Post StatusCode
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=302),
                'should_fail': False,
                'assert': self.assertStatusCode,
            },
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=404),
                'should_fail': True,
                'assert': self.assertStatusCode,
            },
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=302),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            {
                'request': Request(url='/', method=POST),
                'response': Response(status_code=404),
                'should_fail': True,
                'assert': self.assertTrueResponse,
            },
            # Get StatusCode
            {
                'request' : Request(url='/'),
                'response' : Response(status_code=200),
                'should_fail': False,
                'assert': self.assertStatusCode,
            },
            {
                'request': Request(url='/'),
                'response': Response(status_code=404),
                'should_fail': True,
                'assert': self.assertStatusCode,
            },
            {
                'request': Request(url='/'),
                'response': Response(status_code=200),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            {
                'request': Request(url='/'),
                'response': Response(status_code=404),
                'should_fail': True,
                'assert': self.assertTrueResponse,
            },
            # Value in Context
            {
                'request': Request(url='/'),
                'response': Response(in_context='title'),
                'should_fail': False,
                'assert': self.assertValueInContext,
            },
            {
                'request': Request(url='/'),
                'response': Response(in_context='not_in_context_key'),
                'should_fail': True,
                'assert': self.assertValueInContext,
            },
            {
                'request': Request(url='/'),
                'response': Response(in_context='title'),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            {
                'request': Request(url='/'),
                'response': Response(in_context='not_in_context_key'),
                'should_fail': True,
                'assert': self.assertTrueResponse,
            },
            # Context Value
            {
                'request': Request(url='/'),
                'response': Response(context_values={'title': 'Title'}),
                'should_fail': False,
                'assert': self.assertContextValues,
            },
            {
                'request': Request(url='/'),
                'response': Response(context_values={'title': 'Error value'}),
                'should_fail': True,
                'assert': self.assertContextValues,
            },
            {
                'request': Request(url='/'),
                'response': Response(context_values={'error key': 'Title'}),
                'should_fail': True,
                'assert': self.assertContextValues,
            },
            {
                'request': Request(url='/'),
                'response': Response(context_values={'title': 'Title'}),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
            {
                'request': Request(url='/'),
                'response': Response(context_values={'title': 'Error value'}),
                'should_fail': True,
                'assert': self.assertTrueResponse,
            },
            # Content Value
            {
                'request': Request(url='/'),
                'response': Response(content_values=['Title']),
                'should_fail': False,
                'assert': self.assertContentValues,
            },
            {
                'request': Request(url='/'),
                'response': Response(content_values=[
                    ContentValue(
                        value='Title',
                        count=1
                    )
                ]),
                'should_fail': False,
                'assert': self.assertContentValues,
            },
            {
                'request': Request(url='/'),
                'response': Response(content_values=['Error value']),
                'should_fail': True,
                'assert': self.assertContentValues,
            },
            {
                'request': Request(url='/'),
                'response': Response(content_values=['Title']),
                'should_fail': False,
                'assert': self.assertTrueResponse,
            },
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
            # Create object
            # {
            #     'request': Request(
            #         url='/',
            #         method=POST,
            #         data={'name': 'new_name'}
            #     ),
            #     'response': Response(
            #         created={
            #             'model': Simple,
            #             'fields': {
            #                 'name': 'new_name',
            #             }
            #         },
            #     ),
            #     'should_fail': False,
            #     'assert': self.assertCreated,
            # },
            # {
            #     'request': Request(
            #         url='/',
            #         method=POST,
            #         data={'name': 'new_name'}
            #     ),
            #     'response': Response(
            #         created={
            #             'model': Simple,
            #             'fields': {
            #                 'name': 'error_name',
            #             }
            #         },
            #     ),
            #     'should_fail': True,
            #     'assert': self.assertCreated,
            # },
            # Test Detail View
            # {
            #     'request': Request(
            #         url='/',
            #         create_one={
            #             'model': Simple,
            #             'fields': {
            #                 'name': 'some name',
            #             }
            #         }
            #     ),
            #     'response': Response(status_code=200),
            #     'should_fail': False,
            #     'assert': self.assertStatusCode,
            # },
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
                # self.clear_db()  # TODO: someting wrong with supTests
