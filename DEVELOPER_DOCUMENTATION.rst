Django DRY Tests Developer Documentation
=======================================

Makefile
--------

First, check the **Makefile**. It contains many useful commands to work with the project.

.. include:: Makefile
   :literal:

Main commands
^^^^^^^^^^^^

Run Tests
~~~~~~~~~

.. code-block:: bash

    make test

Tests coverage
~~~~~~~~~~~~~~

.. code-block:: bash

    make coverage

Lint
~~~~

.. code-block:: bash

    make lint

How to Develop a New Feature
---------------------------

Preparation
^^^^^^^^^^^

- Run Django tests. Let them fail.
- Add an example view or something else with the demo project.
- Make the Django tests work.

This step allows you to comfortably create a new feature.

Make a New Feature
^^^^^^^^^^^^^^^^^^

- Add the new feature to the `dry_tests` package.
- Ensure all tests work.
- Check the coverage.
- Run the linter.
- Make a new pull request to contribute.
