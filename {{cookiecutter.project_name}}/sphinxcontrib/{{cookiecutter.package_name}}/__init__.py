"""
    sphinxcontrib.{{ cookiecutter.package_name }}
    ~~~~~~~~~~~~~~{{ '~' * (cookiecutter.project_name|length) }}

    {{ cookiecutter.short_description }}

    :copyright: Copyright 2017 by {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
    :license: BSD, see LICENSE for details.
"""

import pbr.version


__version__ = pbr.version.VersionInfo(
    '{{cookiecutter.package_name}}').version_string()
