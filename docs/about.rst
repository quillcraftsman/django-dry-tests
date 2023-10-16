Django DRY Tests
================

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

Project on `GitHub <https://github.com/quillcraftsman/django-dry-tests>`_

.. start-badges

.. list-table::
    :widths: 15 85
    :stub-columns: 1

    * - Build
      - | |Tests| |Pylint|
    * - Package
      - | |PyPI| |Development status| |License| |Python version| |Wheel|
    * - Support
      - | |Documentation| |Discussions| |Issues|
    * - Stats
      - | |Downloads| |Monthly Downloads| |Weekly Downloads|

.. |Tests| image:: https://github.com/quillcraftsman/django-dry-tests/actions/workflows/run-tests.yml/badge.svg?branch=main
   :target: https://github.com/quillcraftsman/django-dry-tests/actions/workflows/run-tests.yml
.. |Pylint| image:: https://github.com/quillcraftsman/django-dry-tests/actions/workflows/lint.yml/badge.svg?branch=main
   :target: https://github.com/quillcraftsman/django-dry-tests/actions/workflows/lint.yml
.. |Documentation| image:: https://readthedocs.org/projects/django-dry-tests/badge/?version=latest
   :target: http://django-dry-tests.readthedocs.io/en/latest/?badge=latest
.. |Discussions| image:: https://img.shields.io/badge/discussions-ff0068.svg
   :target: https://github.com/quillcraftsman/django-dry-tests/discussions/
.. |Issues| image:: https://img.shields.io/badge/issues-11AE13.svg
   :target: https://github.com/quillcraftsman/django-dry-tests/issues/
.. |PyPI| image:: https://img.shields.io/pypi/v/django-dry-tests.svg
   :target: https://pypi.python.org/pypi/django-dry-tests/
.. |Development status| image:: https://img.shields.io/pypi/status/django-dry-tests.svg
    :alt: Development status
    :target: https://pypi.python.org/pypi/django-dry-tests
.. |Python version| image:: https://img.shields.io/pypi/pyversions/django-dry-tests.svg
   :target: https://pypi.python.org/pypi/django-dry-tests/
.. |License| image:: https://img.shields.io/pypi/l/django-dry-tests
   :target: https://github.com/quillcraftsman/django-dry-tests/blob/main/LICENSE
.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-dry-tests.svg
    :alt: PyPI Wheel
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

- :ref:`Mission`
- :ref:`Open Source Project`
- :ref:`Features`
- :ref:`Requirements`
- :ref:`Development Status`

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

This is the open source project with `MIT license <https://github.com/quillcraftsman/django-dry-tests/blob/main/LICENSE>`_.
Be free to use, fork, clone and contribute.

Features
--------

- Special **Request**, **Response** and **Form** classes to simple set test data
- Special **SimpleTestCase** class with new asserts:
- - The main asserts is **assertTrueResponse** and **assertTrueForm**. You can use this for most cases.
- - Other special asserts:

.. autoclass:: dry_tests.SimpleTestCase
    :members:

- Special **TestCase** class. Similar with **SimpleTestCase** but with testing database (**Not ready yet**)

Requirements
------------

.. include:: ../requirements.txt

Development Status
------------------

.. automodule:: package
    :members:
