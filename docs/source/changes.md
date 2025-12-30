# Changes

This is a record of all past cookiecutter-pytask-project releases and what went into
them in reverse chronological order.

## Unreleased

- {pull}`70` drops support for Python 3.9 and adds support for Python 3.14.
- {pull}`71` switches typing from mypy to ty.
- {pull}`72` updates the pre-commit hooks.
- {pull}`73` removes tox in favor of uv + just.

## 1.8.0 - 2024-12-24

- {pull}`52` updates the template in many different ways. Better pre-commit hooks,
  better integration with pixi, mypy is not optional anymore, etc..

## 1.7.0 - 2024-05-03

- {pull}`39` updates the pre-commit hooks.
- {pull}`41` updates the infrastructure.

## 1.6.0 - 2023-11-23

- {pull}`35` modernizes the template.

## 1.5.0 - 2023-02-04

- {pull}`33` fixes some small things. (Thanks to @hmgaudecker!)
- {pull}`34` adds dependabot to update Github Actions.

## 1.4.0 - 2023-01-01

- {pull}`29` adds ruff and refurb to pre-commits and fixes CI banner.

## 1.3.0 - 2022-11-20

- {pull}`22` removes sphinx-click and renames docs environment to
  `docs_environment.yml`.
- {pull}`25` adds docsformatter.
- {pull}`26` uses a better approach to set the initial branch.
- {pull}`27` adds support for Python 3.11.
- {pull}`28` does some cleaning and deprecates support for Python 3.7. Thanks
  {user}`timmens`!

## 1.2.1 - 2022-05-13

- {pull}`20` fixes some small rendering issues.

## 1.2.0 - 2022-04-14

- {pull}`7` skips concurrent CI builds.
- {pull}`8` harmonizes cookiecutter-pytask-project with econ-project-templates.
- {pull}`9` deprecates Python 3.6, add support for Python 3.10 and add mypy optionally.
- {pull}`12` removes `LICENSE` from `MANIFEST.in` if no license is selected.
- {pull}`13` adds a `.gitignore`.
- {pull}`14` adds a `CITATION`.
- {pull}`15` cancels concurrent CI jobs.
- {pull}`18` fixes {issue}`17` and moves rst to markdown.

## 1.1.0 - 2022-01-16

- {pull}`4` renames the cookiecutter from cookiecutter-pytask to
  cookiecutter-pytask-project to avoid confusion with the cookiecutter for plugins. And
  remove unnecessary packaging stuff.

## 1.0.0 - 2022-01-05

- {pull}`1` creates first release of a minimal cookiecutter template for a pytask
  project.
- {pull}`2` adds more tests.
