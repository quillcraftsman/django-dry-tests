Django DRY Tests
================

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

- :ref:`Mission`
- :ref:`Open Source Project`
- `Features <#features>`_
- :ref:`Requirements`
- :ref:`Development Status`
- :ref:`Install`
- :ref:`Quickstart`
- :ref:`Contributing`

Mission
-------

The mission of the **Django DRY Tests** to design and develop open source python package to test **django**
application

- fast
- with minimal code duplication
- with the ability to use **TDD** easily
- simple and comfortable

Open Source Project
-------------------

This is the open source project with `MIT license <LICENSE>`_.
Be free to use, fork, clone and contribute.

.. _Features:
Features
--------

- Special **Request** and **Response** classes to simple set test data
- Special **SimpleTestCase** class with:

  - `assertTrueResponse(self, current_response, true_response)` - Main assert to compare real response with expected
  - `assertResponsesAreTrue(self, response_pairs)` - Compare many responses
  - Other more simple asserts (``assertStatusCode``, ``assertRedirectUrl``, ``assertValueInContext``,
    ``assertContextValues``, ``assertContentValues``)

- Special **TestCase** class. Similar with **SimpleTestCase** but with testing database (**Not ready yet**)

.. autoclass:: dry_tests.testcases.SimpleTestCase
    :members:

Requirements
------------

.. include:: requirements.txt
   :literal:

Development Status
------------------

.. include:: package_info.py
   :literal:

Package available on `PyPi <https://pypi.org/project/django-dry-tests/>`_

Install
-------

with pip
^^^^^^^^

.. code-block:: bash

   pip install django-dry-tests

from release page
^^^^^^^^^^^^^^^^^

Download source code from `GitHub Releases page <https://github.com/quillcraftsman/django-dry-tests/releases>`_

clone from GitHub
^^^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/quillcraftsman/django-dry-tests.git
   make install

Quickstart
----------

For example, you need to test some view like this:

.. code-block:: python

   def index_view(request):
       if request.method == 'GET':
           context = {
               'title': 'Title'
           }
           return render(request, 'demo/index.html', context)

       name = request.POST.get('name', None)
       if name is not None:
           Simple.objects.create(name=name)
       return HttpResponseRedirect('/')

And you want to check:

- GET response status code
- GET response context data
- GET response some html data
- POST response status code
- POST response redirect url
- POST response save object to database (**Not implemented yet**)

Let's see the tests code:

.. code-block:: python

   from dry_tests import (
       Request,
       TrueResponse as Response,
       SimpleTestCase,
       POST,
   )


   class ViewTestCase(SimpleTestCase):

       def test_main(self):
           data = [
               # Multy parameters GET
               {
                   'request': Request(url='/'),
                   'response': Response(
                       status_code=200,
                       in_context='title',
                       context_values={'title': 'Title'},
                       content_values=['Title'],
                   ),
               },
               # Multy parameters POST
               {
                   'request': Request(url='/', method=POST),
                   'response': Response(
                       status_code=302,
                       redirect_url='/',
                   ),
               },
           ]
           for item in data:
               request = item['request']
               true_response = item['response']
               current_response = request.get_url_response(self.client)
               self.assertTrueResponse(current_response, true_response)

Contributing
------------

You are welcome! To easy start please check:

- :ref:`Developer Guidelines`
- :ref:`Developer Documentation`
- :ref:`Code of Conduct`
- :ref:`Security Policy`
