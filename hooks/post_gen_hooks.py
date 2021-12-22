"""This module contains hooks which are executed after the template is rendered."""
import shutil
import subprocess
import warnings
from pathlib import Path


PROJECT_PATH = Path.cwd()


def remove_file(*filepath):
    """Remove a file."""
    try:
        PROJECT_PATH.joinpath(*filepath).unlink()
    except FileNotFoundError:
        pass


def remove_directory(*filepath):
    """Remove a directory."""
    try:
        path = PROJECT_PATH.joinpath(*filepath)
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def main():
    """Apply post generation hooks."""
    if "{{ cookiecutter.create_changes_file }}" == "no":
        remove_file("CHANGES.rst")

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")

    if "{{ cookiecutter.add_tox }}" == "no":
        remove_directory(".github", "workflows")
        remove_file("tox.ini")

    if "{{ cookiecutter.add_github_actions }}" == "no":
        remove_directory(".github", "workflows")

    if "{{ cookiecutter.add_readthedocs }}" == "no":
        remove_file(".readthedocs.yml")

    subprocess.run(("git", "init"), cwd=PROJECT_PATH, check=True)

    if "{{ cookiecutter.create_conda_environment_at_finish }}" == "yes":
        if shutil.which("mamba") is not None:
            conda_exe = shutil.which("mamba")
        else:
            conda_exe = shutil.which("conda")

        if conda_exe is None:
            warnings.warn(
                "conda environment could not be created since no conda or mamba "
                "executable was found."
            )
        else:
            subprocess.run(("conda", "env", "create"), cwd=PROJECT_PATH, check=True)


if __name__ == "__main__":
    main()
