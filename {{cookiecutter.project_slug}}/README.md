# {{ cookiecutter.project_name }}

{% if cookiecutter.add_github_actions == "yes"
%}[![image](https://img.shields.io/github/actions/workflow/status/{{
cookiecutter.github_username }}/{{ cookiecutter.project_slug
}}/main.yml?branch=main)](https://github.com/{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }}/actions?query=branch%3Amain) {% endif %} {% if
cookiecutter.add_readthedocs == "yes" %}[![image](https://readthedocs.org/projects/{{
cookiecutter.project_slug | replace("_", "-") }}/badge/?version=stable)](https://{{
cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/stable/?badge=stable)
[![image](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{
cookiecutter.github_username }}/{{ cookiecutter.project_slug }}) {% endif %}
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/{{
cookiecutter.github_username }}/{{ cookiecutter.project_slug
}}/main.svg)](https://results.pre-commit.ci/latest/github/{{
cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/main)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Usage

To get started, create the environment with

```console
$ mamba env create
```

To build the project, type

```console
$ pytask
```

## Credits

This project was created with [cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[cookiecutter-pytask-project](https://github.com/pytask-dev/cookiecutter-pytask-project)
template.
