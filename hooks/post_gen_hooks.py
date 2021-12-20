import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(*filepath):
    try:
        PROJECT_DIRECTORY.joinpath(*filepath).unlink()
    except FileNotFoundError:
        pass


def remove_directory(*filepath):
    try:
        path = PROJECT_DIRECTORY.joinpath(*filepath)
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def main():
    if "{{ cookiecutter.create_changes_file }}" == "no":
        remove_file("CHANGES.rst")

    if "{{ cookiecutter.add_tox }}" == "no":
        remove_directory(".github", "workflows")
        remove_file("tox.ini")

    if "{{ cookiecutter.add_github_actions }}" == "no":
        remove_directory(".github", "workflows")

    if "{{ cookiecutter.add_readthedocs }}" == "no":
        remove_file(".readthedocs.yml")


if __name__ == "__main__":
    main()
