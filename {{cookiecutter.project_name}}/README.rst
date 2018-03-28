{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_org }}/{{  cookiecutter.project_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_org }}/{{  cookiecutter.project_name }}

{{ cookiecutter.short_description}}

Overview
--------

Add a longer description here.

Links
-----

- Source: https://github.com/{{ cookiecutter.github_org }}/{{  cookiecutter.project_name }}
- Bugs: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_name }}/issues
