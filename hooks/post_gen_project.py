"""Contains hooks which are executed after the template is rendered."""

from __future__ import annotations

import shutil
import subprocess
from contextlib import suppress
from pathlib import Path


def remove_file(*filepath: str | Path) -> None:
    """Remove a file."""
    with suppress(FileNotFoundError):
        Path(*filepath).unlink()


def remove_directory(*filepath: str | Path) -> None:
    """Remove a directory."""
    with suppress(FileNotFoundError):
        path = Path(*filepath)
        shutil.rmtree(path)


def main() -> None:
    """Apply post generation hooks."""
    project_path = Path.cwd()

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file(project_path, "LICENSE")

    if "{{ cookiecutter.add_tox }}" == "no":
        remove_directory(project_path, ".github", "workflows")
        remove_file("tox.ini")

    if "{{ cookiecutter.add_github_actions }}" == "no":
        remove_directory(project_path, ".github", "workflows")

    if "{{ cookiecutter.add_readthedocs }}" == "no":
        remove_file(project_path, ".readthedocs.yaml")

    subprocess.run(
        ("git", "init", "--initial-branch", "main"),
        check=True,
        capture_output=True,
    )

    if "{{ cookiecutter.make_initial_commit }}" == "yes":
        # Create an initial commit on the main branch and restore global default name.
        subprocess.run(
            ("git", "config", "user.name", "'{{ cookiecutter.github_username }}'"),
            check=True,
        )
        subprocess.run(
            ("git", "config", "user.email", "'{{ cookiecutter.github_email }}'"),
            check=True,
        )
        subprocess.run(("git", "add", "."), check=True)
        subprocess.run(
            ("git", "commit", "-m", "'Initial commit.'"),
            check=True,
            capture_output=True,
        )


if __name__ == "__main__":
    main()
