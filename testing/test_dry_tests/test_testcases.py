"""
Test for testcases
"""
from dry_tests.testcases import mock


def test_mock():
    """
    Test mock
    :return:
    """
    assert mock() == 'mock'
