Testing
=======

Dependencies are managed with `uv`_.

.. _uv: https://docs.astral.sh/uv/

Install dependencies
--------------------
Dependencies can be installed via the command below.

.. code-block:: bash

    $ make requirements

Run tests
--------------------
The command below runs the Python tests.

.. code-block:: bash

    $ uv run make test

Code quality validation can be run independently with:

.. code-block:: bash

    $ uv run make quality
