# Quick Reference

Apply this Copier template to an existing [`able-workflow-copier`]({{ able_workflow_copier_docs }}) project (i.e., `./`) to create a `datasets/`, `features/`, or `models/` module in the python package with the following commands:

```bash
copier copy --trust {{ able_workflow_module_copier_repo }}.git ./
```

{% raw %}

If this template has been updated and you would like to apply those updates to your project, run the following command replacing `{{ module_type }}` and `{{ module_name }}` with the module you would like to update. You can see all the Copier templates that have been applied to your project in the `./copier-answers/` directory. (DO NOT EDIT THESE FILES.)

```bash
copier update --trust --answers-file ".copier-answers/module-{{ module_type }}-{{ module_name }}.yml" ./
```

{% endraw %}
