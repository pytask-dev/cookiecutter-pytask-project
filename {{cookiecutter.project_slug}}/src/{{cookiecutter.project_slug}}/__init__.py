"""Contains the main namespace of {{ cookiecutter.project_slug }}."""

# Import the version from _version.py which is dynamically created by setuptools-scm
# when the project is installed with ``pip install -e .``. Do not put it into version
# control!
try:
    from ._version import version as __version__  # ty: ignore[unresolved-import, unused-ignore-comment]
except ImportError:
    __version__ = "unknown"


__all__ = ["__version__"]
