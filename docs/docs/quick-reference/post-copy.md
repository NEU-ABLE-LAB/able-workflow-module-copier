---
render_macros: false
---

# Post-Copy Checklist

??? note "Audience: Project Developers"

    This checklist is for project developers adding a new module to an existing workflow project.
    It assumes you will update committed project files, tests, and documentation in the target repository.

After running `copier copy`, see `.copier-answers/post-copier-todos/module-{{ module_type }}-{{ module_name }}.md` for next steps on implementing your module in the project. You can copy-paste the contents of that file into a GitHub issue or a project management tool to track the implementation of the module.

{%
    include-markdown "../../../template/.copier-answers/post-copier-todos/module-{{ module_type }}-{{ module_name }}.md.jinja"
    heading-offset=1
%}
