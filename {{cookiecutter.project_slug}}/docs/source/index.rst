Welcome to {{ cookiecutter.project_name }}'s documentation!
{% for _ in range(cookiecutter.project_name | length + 28) %}={% endfor %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   changes
   api
