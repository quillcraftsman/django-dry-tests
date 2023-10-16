Django DRY Tests
================

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

Project on `GitHub <https://github.com/quillcraftsman/django-dry-tests>`_

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
- Special **SimpleTestCase** and **TestCase** classes with new asserts:
- - The main asserts is **assertTrueResponse** and **assertTrueForm**. You can use this for most cases.
- - Other special asserts:

.. autoclass:: dry_tests.testcases.TestCaseMixin
    :members:

Requirements
------------

.. include:: ../requirements.txt

Development Status
------------------

.. automodule:: package
    :members:
