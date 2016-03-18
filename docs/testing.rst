Testing
=======

If you have not already done so, create/activate a `virtualenv`_. Unless otherwise stated, assume all terminal code
below is executed within the virtualenv.

.. _virtualenv: https://virtualenvwrapper.readthedocs.org/en/latest/

Install dependencies
--------------------
Dependencies can be installed via the command below.

.. code-block:: bash

    $ make requirements

Run tests
--------------------
The command below runs the Python tests and code quality validation—Pylint and PEP8.

.. code-block:: bash

    $ make validate

Code quality validation can be run independently with:

.. code-block:: bash

    $ make quality
