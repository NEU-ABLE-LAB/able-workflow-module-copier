# Changelog

Human-readable log of changes between versions. Follows the [Common Changelog style guide](https://common-changelog.org/).

## dev

### Changed

### Added

- Added regression test coverage for `tasks/append_config_include.py` to ensure list indentation is preserved when appending to `configfile`.

### Removed

### Fixed

- Preserved indented YAML sequence formatting in `workflow/profiles/default/config.yaml` when `tasks/append_config_include.py` appends a config include.

## v0.1.2 - 2026-03-18

### Changed

- Split `pr.yml` into `main.yml` to keep codecov secrets out of PRs
- Limited `mkdocs<2` due to breaking change in 2.0 (#26)
- Enforced uniformity of scripts and tests across `able-workflow*-copier` repos
- `sandbox_examples_generate` is now module `scripts.sandbox_examples_generate` instead of script
- Synced the sandbox template snapshot with the root dry-run manifest layout (`data/tests/dry-run/`, `include:`, and `touch:`).
- Consolidated `.github/workflows/pr.yml` and `.github/workflows/main.yml` into `.github/workflows/ci.yml`, with Codecov secrets only used on pushes to `main`.
- Updated CI badge links in `README.md` and `docs/docs/index.md` to reference `.github/workflows/ci.yml`.
- Updated contributing docs references from `.github/workflows/pr.yml` to `.github/workflows/ci.yml`.

### Added

- Refactored `copie_helpers.py` functions into their own file.

### Removed

### Fixed

- typos

## 0.1.1 - 2026-03-14

### Changed

- Updated sandbox checkout ref in `.github/workflows/pr.yml` for `able-workflow-copier` integration tests.
- Updated docs site defaults in `docs/mkdocs.yml` to `neu-able-lab.github.io` URLs and configured `git-revision-date-localized` locale (`en`).
- Updated dependency specs in `pyproject.toml` and `environment-py312-dev.yaml`:
  - `copier-templates-extensions` -> `copier-template-extensions>=0.3.3`
  - `pytest-copie` (git URL) -> `pytest-copie>=0.3.1`
- Updated Ruff config in `pyproject.toml` from `exclude` to `extend-exclude` for `template`.
- `mike` sets `mkdocs` version aliases `dev` for last commit on `main` and `latest` for last release

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
