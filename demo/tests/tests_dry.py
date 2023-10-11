"""
Tests with Django Dry Tests TestCase
"""
from dry_tests import Request, Response, SimpleTestCase, POST
# from .db_test_data import create_simple
# from demo.models import Simple


class ViewTestCase(SimpleTestCase):
    """
    Concrete TestCase inherited from DRY SimpleTestCase
    """

    def test_main(self):
        """
        All asserts tests in one test function
        :return:
        """
        data = [
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
            # Content Value
            {
                'request': Request(url='/'),
                'response': Response(content_value='Title'),
                'should_fail': False,
                'assert': self.assertContentValue,
            },
            {
                'request': Request(url='/'),
                'response': Response(content_value='Error value'),
                'should_fail': True,
                'assert': self.assertContentValue,
            },
            # url_args
            {
                'request': Request(
                    url='/query/',
                    url_args=['kwarg_value'],
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
                    url='/query/',
                    url_args=['kwarg_value'],
                    url_params={
                        'a': 'x',
                        'b': 'y',
                    }
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
            response = item['response']
            assert_function = item['assert']
            with self.subTest(msg=str(item)):
                # self.setUp()
                # self.setUpClass()
                # self.setUpTestData()
                # self.clear_db()
                if item['should_fail']:
                    with self.assertRaises(AssertionError):
                        assert_function(item['request'], item['response'])
                else:
                    assert_function(request, response)
                # self.clear_db()  # TODO: someting wrong with supTests
                # self.tearDown()
                # self.tearDownClass()
