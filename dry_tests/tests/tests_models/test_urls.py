"""
Tests for urls
"""
from django.test import SimpleTestCase, tag
from dry_tests.models.urls import Url


@tag('dry')
class UrlTestCase(SimpleTestCase):
    """
    Tests for Url
    """

    def test_make_url(self):
        """
        Make with url only
        :return:
        """
        self.assertEqual(Url('/').make_url(), '/')

    def test_make_url_with_args(self):
        """
        Make with args
        :return:
        """
        self.assertEqual(
            Url('/', args=['one', 'two']).make_url(),
            '/one/two/',
        )

    def test_make_url_with_unique_params(self):
        """
        Make with unique params
        :return:
        """
        self.assertEqual(
            Url('/', params={
                'one': 'one',
                'two': 'two',
            }).make_url(),
            '/?one=one&two=two',
        )

    def test_make_url_with_same_params(self):
        """
        Make with same params
        :return:
        """
        self.assertEqual(
            Url('/', params={
                'one': ('one', 'two'),
                'two': 'two',
            }).make_url(),
            '/?one=one&one=two&two=two',
        )

    def test_make_url_wrong_type_params(self):
        """
        Error parameter value
        :return:
        """
        with self.assertRaises(ValueError):
            Url('/', params={  # pylint: disable=expression-not-assigned
                    'one': ['one', 'two'],
                    'two': 'two',
                }).make_url(),  # pylint: disable=trailing-comma-tuple
