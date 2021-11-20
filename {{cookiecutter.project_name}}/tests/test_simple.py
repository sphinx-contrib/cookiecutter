# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764
import pytest
from sphinx.testing.util import SphinxTestApp


def test(app: SphinxTestApp) -> None:
    # app is a Sphinx application object for default sphinx project
    # (tests/cases/test-root)

    # See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-974680232
    app.warningiserror = app.keep_going = True

    app.build()


@pytest.mark.sphinx(buildername="latex")
def test_latex(app: SphinxTestApp) -> None:
    # latex builder is chosen here
    app.build()


@pytest.mark.sphinx(testroot="myst")
def test_myst(app: SphinxTestApp) -> None:
    # app is a Sphinx application for myst sphinx project
    # (tests/cases/test-myst)
    app.build()


@pytest.mark.sphinx(confoverrides={"html_theme": "furo"})
def test_confoverrides(app: SphinxTestApp) -> None:
    # a Sphinx application configured with given setting
    app.build()
