from __future__ import annotations

import {{ cookiecutter.project_slug }}


def test_import():
    assert hasattr({{ cookiecutter.project_slug }}, "__version__")
