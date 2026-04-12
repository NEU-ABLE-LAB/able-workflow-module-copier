# ABLE Workflow Module Copier

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Common Changelog](https://common-changelog.org/badge.svg)](https://common-changelog.org)
[![codecov](https://codecov.io/gh/NEU-ABLE-LAB/able-workflow-module-copier/graph/badge.svg?token=DQ6OMZF5HZ)](https://codecov.io/gh/NEU-ABLE-LAB/able-workflow-module-copier)
[![tox Main Tests](https://github.com/NEU-ABLE-LAB/able-workflow-module-copier/actions/workflows/ci.yml/badge.svg)](https://github.com/NEU-ABLE-LAB/able-workflow-module-copier/actions/workflows/ci.yml)

A [copier](https://copier.readthedocs.io/en/stable/) template for adding a datasets, features, or models module to an existing ABLE Workflow project.

This template assumes that you have already created an [`able-workflow-copier`]({{ able_workflow_copier_docs }}) project.

## Start Here

1. If you want to add a new module to an existing project, start with [Quick Reference](quick-reference/).
2. If you need the ecosystem-level rationale behind the ABLE Workflow templates, go back to the main [`able-workflow-copier` Overview]({{ able_workflow_copier_docs }}/overview/).
3. If you are maintaining this template repository itself, use [Contributing](contributing/).

## What This Template Adds

- A new `datasets`, `features`, or `models` module inside the project's Python package.
- The matching configuration and schema locations for that module.
- The docs and contributing-template fragments that get inserted into the generated project's documentation.

## Template Ecosystem

- [`able-workflow-copier`]({{ able_workflow_copier_docs }})
- [`able-workflow-module-copier`]({{ able_workflow_module_copier_docs }})
- [`able-workflow-etl-copier`]({{ able_workflow_etl_copier_docs }})
- [`able-workflow-rule-copier`]({{ able_workflow_rule_copier_docs }})

Project users and project integrators should primarily use the generated project's documentation instead of this template repository.
