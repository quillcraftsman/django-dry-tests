"""
Tests with Django Dry Tests TestCase
"""
from dry_tests import Request, Response, TestCase, POST


class ViewTestCase(TestCase):

    def test_main(self):
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
        ]

        for item in data:
            request = item['request']
            response = item['response']
            assert_function = item['assert']
            with self.subTest(msg=str(item)):
                if item['should_fail']:
                    with self.assertRaises(AssertionError):
                        assert_function(item['request'], item['response'])
                else:
                    assert_function(request, response)