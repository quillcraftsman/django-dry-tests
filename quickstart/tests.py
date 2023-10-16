"""
Tests with django-dry-tests
"""
from django.test import tag
from dry_tests import (
    SimpleTestCase,
    Request,
    TrueResponse,
    Context,
)


@tag('dry')
class QuickStartViewSimpleTestCase(SimpleTestCase):
    """
    SimpleTestCase example
    """

    def test_get(self):
        """
        Test Example with django-dry-tests
        :return:
        """
        # Create Request Model
        request = Request(
            url='/quickstart/'
        )

        # Create Response Model to check all view.
        # You can set only one param without others to check it.
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['quickstart'],  # check that quickstart key in context
                values=['Quickstart'],  # check that "Quickstart" value in context
                items={
                    'quickstart': 'Quickstart'
                },  # check both keys and values in context
                types={
                    'quickstart': str
                }  # check values types without check values
            ),
            content_values = [
                'Quickstart',
                '<h1>Quickstart title</h1>'
            ],  # check values after template will be rendered
        )

        # get url response with Django default Test Client
        current_response = request.get_response(self.client)
        # Use main assert to run all asserts
        self.assertTrueResponse(current_response, true_response)
        # Relax and enjoy then
