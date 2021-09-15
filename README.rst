===================
cookiecutter-sphinx
===================

A `cookiecutter`_ template for a `Sphinx extension`_ within the
`sphinxcontrib`_ namespace.

This template focuses on setting up the scaffolding of the project: for
information on actually writing your plugin, refer to the `Sphinx
documentation`_.

Features
--------

- `pbr`_ for simple packaging.
- `pytest`_ for testing.
- `tox`_ for automation of test runners and other stuff.

Other stuff we include:

- `Travis CI`_ support for unit tests (using the `tox-travis`_ plugin).
- `mypy`_ integration for type annotations.
- `yapf`_\-based automatic Python code formatting.

Usage
-----

Install `cookiecutter`::

    pip install cookiecutter

Generate a Python package::

    cookiecutter https://github.com/sphinx-contrib/cookiecutter.git

Next steps:

- Create a GitHub repo for your project and push your code.

- Read `CONTRIBUTING <CONTRIBUTING.rst>`__ for information on submitting the
  package to the `sphinx-contrib` organization.

License
-------

`Apache License, Version 2.0 <LICENSE>`__

.. _cookiecutter: https://github.com/audreyr/cookiecutter/
.. _Sphinx extension: http://www.sphinx-doc.org/en/stable/extdev/
.. _sphinxcontrib: https://github.com/sphinx-contrib
.. _Sphinx documentation: http://www.sphinx-doc.org/en/master/
.. _pbr: https://docs.openstack.org/pbr/latest/
.. _pytest: https://docs.pytest.org/en/latest/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Travis CI: https://travis-ci.org/
.. _tox-travis: https://github.com/tox-dev/tox-travis
.. _mypy: http://mypy.readthedocs.io/en/latest/
.. _yapf: https://github.com/google/yapf
