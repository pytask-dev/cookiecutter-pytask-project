"""This module contains hooks which are executed before the template is rendered."""
import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]*$"
ENVIRON_REGEX = r"^[-_a-zA-Z0-9]*$"
PYTHONVERSION_REGEX = r"^(3\.(10|[7-9])(\.[0-9]{1,2})?)$"
PYTHONVERSION_MIN = "3.7"

EXCEPTION_MSG_MODULE_NAME = """
ERROR: The project slug ({module_name}) is not a valid Python module name.

Please do not use anything other than letters, numbers, and underscores '_'.
The first character must not be a number.
"""

EXCEPTION_MSG_ENVIRON_NAME = """
ERROR: The project slug ({environment_name}) is not a valid conda environment name.

Please do not use anything other than letters, numbers, underscores '_',
and minus signs '-'.
"""

EXCEPTION_MSG_PYTHONVERSION = f"""
ERROR: The python version must be >= {PYTHONVERSION_MIN}, got {{python_version}}.
"""


def main() -> None:
    """Apply pre-generation hooks."""
    module_name = "{{ cookiecutter.project_slug}}"

    if not re.match(MODULE_REGEX, module_name):
        raise ValueError(EXCEPTION_MSG_MODULE_NAME.format(module_name=module_name))

    environment_name = "{{ cookiecutter.conda_environment_name }}"

    if not re.match(ENVIRON_REGEX, environment_name):
        raise ValueError(EXCEPTION_MSG_ENVIRON_NAME.format(environment_name=environment_name))

    python_version = "{{ cookiecutter.python_version }}"

    if not re.match(PYTHONVERSION_REGEX, python_version):
        raise ValueError(
            EXCEPTION_MSG_PYTHONVERSION.format(python_version=python_version)
        )


if __name__ == "__main__":
    main()
