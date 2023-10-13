Django DRY Tests
================

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

- `Full Documentation <https://drytests.craftsman.lol>`_
- `Mission <#mission>`_
- `Open Source Project <#open-source-project>`_
- `Features <#features>`_
- `Requirements <#requirements>`_
- `Development Status <https://drytests.craftsman.lol#development-status>`_
- `Install <#install>`_
- `Quickstart <https://drytests.craftsman.lol#quickstart>`_
- `Contributing <#contributing>`_

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

Features
--------

- Special **Request** and **Response** classes to simple set test data
- Special **SimpleTestCase** class with:

  - `assertTrueResponse(self, current_response, true_response)` - Main assert to compare real response with expected
  - `assertResponsesAreTrue(self, response_pairs)` - Compare many responses
  - Other more simple asserts (See more in Full Documentation)

- Special **TestCase** class. Similar with **SimpleTestCase** but with testing database (**Not ready yet**)

Requirements
------------

- `Django==4` (Lower versions haven't been tested)

See more in Full Documentation

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

Contributing
------------

You are welcome! To easy start please check:

- `Developer Guidelines <CONTRIBUTING.md>`_
- `Developer Documentation <DEVELOPER_DOCUMENTATION.md>`_
- `Code of Conduct <CODE_OF_CONDUCT.md>`_
- `Security Policy <SECURITY.md>`_
