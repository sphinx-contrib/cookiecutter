# In the absence of official documentation,
# this is a good scaffolding
# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764

import pytest

# Could this be replaced by stdlib pathlib?
# See https://github.com/sphinx-doc/sphinx/issues/9524#issuecomment-895412145
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"

# See https://github.com/dbader/pytest-mypy/issues/123
collect_ignore = ["./cases/"]


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "cases"


@pytest.fixture()
def app(app):
    # See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-974691469
    app.warningiserror = app.keep_going = True
    return app
