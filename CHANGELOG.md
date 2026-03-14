# Changelog

Human-readable log of changes between versions. Follows the [Common Changelog style guide](https://common-changelog.org/).

## 0.1.0-dev

### Changed

- Updated sandbox checkout ref in `.github/workflows/pr.yml` for `able-workflow-copier-dev` integration tests.
- Updated docs site defaults in `docs/mkdocs.yml` to `neu-able-lab.github.io` URLs and configured `git-revision-date-localized` locale (`en`).
- Updated dependency specs in `pyproject.toml` and `environment-py312-dev.yaml`:
  - `copier-templates-extensions` -> `copier-template-extensions>=0.3.3`
  - `pytest-copie` (git URL) -> `pytest-copie>=0.3.1`
- Updated Ruff config in `pyproject.toml` from `exclude` to `extend-exclude` for `template`.

### Added

- Added `vcs_ref` support to test copier runs in `tests/template/conftest.py`.
- Added template git hygiene and pinning checks in `tests/template/tox/test_tox_envs.py`:
  - fail fast when template repo is dirty
  - resolve and use immutable `HEAD` refs for package/module template rendering

### Removed

- Removed `python-envs.pythonProjects` from `.vscode/settings.json`.

### Fixed

- Fixed Copier Jinja extension loader path in `copier.yml` (`copier_template_extensions.TemplateExtensionLoader`).
- Fixed `package_name` default wiring in `copier.yml` to pull from `_external_data.parent_project_tpl.package_name`.
- Fixed invalid-config Snakemake test assertion to validate errors from either `stderr` or `stdout`.

## 0.1.0 - 2025-07-23

Initial commit to public `able-workflow-module-copier` repository from `NEU-ABLE-LAB` private repository.
