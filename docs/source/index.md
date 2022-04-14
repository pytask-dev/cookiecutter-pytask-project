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
$ pip install cookiecutter

$ conda install -c conda-forge cookiecutter
```

Then, set up the template with

```console
$ cookiecutter https://github.com/pytask-dev/cookiecutter-pytask-project
```

## FAQ

Q: Why are the source files nested in `src/<project_slug>`?

A: This is called the src layout and the advantages are discussed in this
[article by Hynek Schlawack](https://hynek.me/articles/testing-packaging/).

Although the article discusses the src layout in terms of Python packages, it is also
beneficial to structure a project the same way. Next to the reasons discussed there, it
is possible to use a single Python environment for multiple projects without messing
with your PYTHONPATH (via `pip install -e .` or `conda develop .`) each time and still
import modules.

```{toctree}
---
caption: 'Contents:'
maxdepth: 1
---
changes
api
```
