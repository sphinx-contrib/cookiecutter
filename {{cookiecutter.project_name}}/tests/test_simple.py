# See https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764
import pytest


def test(app):
    # app is a Sphinx application object for default sphinx project (`tests/cases/test-root`)
    app.build()


@pytest.mark.sphinx(buildername="latex")
def test_latex(app):
    # latex builder is chosen here
    app.build()


@pytest.mark.sphinx(testroot="myst")
def test_case1(app):
    # app is a Sphinx application for case1 sphinx project (`tests/cases/test-case1`)
    app.build()


@pytest.mark.sphinx(confoverrides={"master_doc": "content"})
def test_confoverrides(app):
    # a Sphinx application configured with given setting
    app.build()
