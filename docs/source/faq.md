# FAQ

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
