# Welcome to cookiecutter-pytask-project's documentation!

[![MIT license](https://img.shields.io/github/license/pytask-dev/cookiecutter-pytask-project)](https://github.com/pytask-dev/cookiecutter-pytask-project)
[![image](https://readthedocs.org/projects/cookiecutter-pytask-project/badge/?version=latest)](https://cookiecutter-pytask-project.readthedocs.io/en/latest)
[![image](https://img.shields.io/github/workflow/status/pytask-dev/cookiecutter-pytask-project/main/main)](https://github.com/pytask-dev/cookiecutter-pytask-project/actions?query=branch%3Amain)
[![image](https://codecov.io/gh/pytask-dev/cookiecutter-pytask-project/branch/main/graph/badge.svg)](https://codecov.io/gh/pytask-dev/cookiecutter-pytask-project)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pytask-dev/cookiecutter-pytask-project/main.svg)](https://results.pre-commit.ci/latest/github/pytask-dev/cookiecutter-pytask-project/main)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains a minimal cookiecutter template for a project with
[pytask](https://github.com/pytask-dev/pytask).

## Usage

First, install cookiecutter.

```console
pip install cookiecutter

conda install -c conda-forge cookiecutter
```

Then, set up the template with

```console
cookiecutter https://github.com/pytask-dev/cookiecutter-pytask-project
```

## Features

- [pixi](https://pixi.sh/latest/) as the environment and package manager.

## FAQ

Q: Why are the source files nested in `src/<project_slug>`?

A: This is called the src layout and the advantages are discussed in this
[article by Hynek Schlawack](https://hynek.me/articles/testing-packaging/).

Although the article discusses the src layout in terms of Python packages, it is also
beneficial to structure a project the same way. Next to the reasons discussed there, it
is possible to use a single Python environment for multiple projects without messing
with your PYTHONPATH (via `pip install -e .` or `conda develop .`) each time and still
import modules.

Q: My project is a Python package, but it does not seem to have a version. Where is it?

A: The cookiecutter uses [setuptools_scm](https://github.com/pypa/setuptools_scm/) to
manage the version number. When you install your created project as a Python package
with `pip install -e .`, setuptools_scm tries to infer the version number from the tags
created on the repo.

For example, if you have switched to a commit associated with the tag `v0.2.0`,
setuptools_scm will create a `src/<package_slug>/_version.py` with a variable containing
`version = '0.2.0'` which you can use in your `src/<package_slug>/__init__.py`. If you
are one commit ahead of the tag, you version will be something like `0.2.0.dev1+...`
indicating you are one commit ahead of the tag `v0.2.0`.

If you want to switch to the tradition setup, replace the following code in your
`pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.0"]
```

with

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

```{toctree}
---
caption: 'Contents:'
maxdepth: 1
---
changes
```
