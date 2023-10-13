Django DRY Tests
================

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

.. start-badges

.. list-table::
    :widths: 15 85
    :stub-columns: 1

    * - Build
      - | |Tests|
    * - Docs
      - | |Documentation|
    * - Package
      - | |PyPI| |PyPI version| |Wheel| |Supported implementations|
    * - Support
      - | |Discussions|
    * - Stats
      - | |Downloads| |Monthly Downloads| |Weekly Downloads|

.. |Discussions| image:: https://img.shields.io/badge/discussions-ff0068.svg
   :target: https://github.com/quillcraftsman/django-dry-tests/discussions/
.. |Tests| image:: https://github.com/quillcraftsman/django-dry-tests/actions/workflows/run-tests.yml/badge.svg?branch=main
   :target: https://github.com/quillcraftsman/django-dry-tests/actions/workflows/run-tests.yml
.. |Documentation| image:: https://readthedocs.org/projects/django-dry-tests/badge/?version=latest
   :target: http://django-dry-tests.readthedocs.io/en/latest/?badge=latest
.. |PyPI| image:: https://img.shields.io/pypi/v/django-dry-tests.svg
   :target: https://pypi.python.org/pypi/django-dry-tests/
.. |PyPI version| image:: https://img.shields.io/pypi/pyversions/django-dry-tests.svg
   :target: https://pypi.python.org/pypi/django-dry-tests/
.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-dry-tests.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-dry-tests
.. |Supported implementations| image:: https://img.shields.io/pypi/implementation/django-dry-tests.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-dry-tests
.. |Downloads| image:: https://static.pepy.tech/badge/find-similar
    :alt: Downloads
    :target: https://pepy.tech/project/django-dry-tests
.. |Monthly Downloads| image:: https://img.shields.io/pypi/dm/django-dry-tests.svg
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/django-dry-tests
.. |Weekly Downloads| image:: https://img.shields.io/pypi/dw/django-dry-tests.svg
    :alt: Weelkly Downloads
    :target: https://pepy.tech/project/django-dry-tests

.. end-badges

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
^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/quillcraftsman/django-dry-tests.git
   make install

.. include:: INSTALL.rst

Contributing
------------

You are welcome! To easy start please check:

- `Developer Guidelines <CONTRIBUTING.md>`_
- `Developer Documentation <DEVELOPER_DOCUMENTATION.md>`_
- `Code of Conduct <CODE_OF_CONDUCT.md>`_
- `Security Policy <SECURITY.md>`_
