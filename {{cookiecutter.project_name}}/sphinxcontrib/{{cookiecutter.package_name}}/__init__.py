"""
    sphinxcontrib.{{ cookiecutter.package_name }}
    ~~~~~~~~~~~~~~{{ '~' * (cookiecutter.project_name|length) }}

    {{ cookiecutter.short_description }}

    :copyright: Copyright 2017 by {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
    :license: BSD, see LICENSE for details.
"""

import pbr.version

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo(
    '{{cookiecutter.package_name}}').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    return {'version': __version__, 'parallel_read_safe': True}
