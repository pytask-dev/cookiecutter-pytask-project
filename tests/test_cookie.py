import os
import sys

import pytest


def test_bake_project(cookies):
    major, minor = sys.version_info[:2]
    python_version = f"{major}.{minor}"

    result = cookies.bake(
        extra_context={"project_slug": "helloworld", "python_version": python_version}
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()


def test_remove_readthedocs(cookies):
    result = cookies.bake(extra_context={"add_readthedocs": "no"})

    rtd_config = result.project_path.joinpath(".readthedocs.yaml")
    readme = result.project_path.joinpath("README.rst").read_text()

    assert result.exit_code == 0
    assert result.exception is None

    assert rtd_config.exists()
    assert "readthedocs" not in readme


def test_remove_github_actions(cookies):
    result = cookies.bake(extra_context={"add_github_actions": "no"})

    ga_config = result.project_path.joinpath(".github", "workflows", "main.yml")
    readme = result.project_path.joinpath("README.rst").read_text()

    assert result.exit_code == 0
    assert result.exception is None

    assert ga_config.exists()
    assert "azure" not in readme


@pytest.mark.skipif(
    "CI" not in os.environ, reason="Conda environment is only created on CI service."
)
def test_check_conda_environment_creation(cookies):
    result = cookies.bake(
        extra_context={
            "create_conda_environment_at_finish": "yes",
            "conda_environment_name": "test",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
