Forms testing
-------------

For example, You want to test this django Form:

.. literalinclude:: ../quickstart/forms.py
   :pyobject: ExampleForm

This is the test. We use **TrueForm** model and **assertTrueForm**:

.. literalinclude:: ../quickstart/tests_forms.py
   :pyobject: ExampleFromTestCase