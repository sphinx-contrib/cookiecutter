# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764
import pytest


def test(app):
    # app is a Sphinx application object for default sphinx project
    # (tests/cases/test-root)
    app.build()


@pytest.mark.sphinx(buildername="latex")
def test_latex(app):
    # latex builder is chosen here
    app.build()


@pytest.mark.sphinx(testroot="myst")
def test_myst(app):
    # app is a Sphinx application for myst sphinx project
    # (tests/cases/test-myst)
    app.build()


@pytest.mark.sphinx(confoverrides={"html_theme": "furo"})
def test_confoverrides(app):
    # a Sphinx application configured with given setting
    app.build()
