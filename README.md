# cookiecutter-sphinx-ext

A [cookiecutter] template for a [Sphinx extension].

This template focuses on setting up the scaffolding of the project: for
information on actually writing your plugin, refer to the [Sphinx
documentation][sphinx documentation].

## Features

- [flit] for simple packaging.
- [pytest] for testing.
- [tox] for automation of test runners and other stuff.

Other stuff we include:

- [GitHub Actions] for continuous integration.
- [mypy] integration for type annotations.
- [black] for automatic Python code formatting.

## Usage

Install `cookiecutter`:

```
pip install cookiecutter
```

Generate a Python package:

```
cookiecutter https://github.com/astrojuanlu/cookiecutter-sphinx-ext.git
```

## License

[Apache License, Version 2.0](LICENSE)

[cookiecutter]: https://github.com/audreyr/cookiecutter/
[mypy]: http://mypy.readthedocs.io/
[flit]: https://flit.readthedocs.io/
[pytest]: https://docs.pytest.org/
[sphinx documentation]: http://www.sphinx-doc.org/
[sphinx extension]: http://www.sphinx-doc.org/en/stable/extdev/
[tox]: https://tox.readthedocs.io/en/latest/
[black]: https://black.readthedocs.io/
[GitHub Actions]: https://github.com/features/actions
