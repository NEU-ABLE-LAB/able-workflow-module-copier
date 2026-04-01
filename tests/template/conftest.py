"""
Pytest configuration that mirrors the **parent → child** rendering
implemented in `scripts.sandbox_examples_generate`.

For each directory under `example-answers/<name>/` containing
  • `package.yml` - answers for the *package* template
  • `module.yml`    - answers for the *module*   template
we first render the package template (able-workflow-copier),
then render this repository's module template with
``parent_result`` pointing to the package output.

The test fixture yields ``(project_dir, example_name)`` exactly like before.
"""

from __future__ import annotations

import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, cast

import pytest
from loguru import logger
from ruamel.yaml import YAML

from scripts.copie_helpers import (
    load_module_from_path,
    make_copier_config,
    new_copie,
    run_copie_with_output_control,
)

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
ensure_package_repo_path = PROJECT_ROOT / "scripts" / "pull_able_workflow_copier.py"
module = load_module_from_path(ensure_package_repo_path)
ensure_package_template_repo = module.ensure_package_template_repo


# ─────────────────────────────────────────────────────────────────────────────
# Static paths
# ─────────────────────────────────────────────────────────────────────────────


TEMPLATE_PACKAGE_DIR = ensure_package_template_repo(PROJECT_ROOT)
TEMPLATE_MODULE_DIR = PROJECT_ROOT


# ─────────────────────────────────────────────────────────────────────────────
# Example discovery
# ─────────────────────────────────────────────────────────────────────────────


@dataclass
class Example:
    name: str
    package_answers: Dict[str, Any]
    module_answers: Dict[str, Any]


def _read_yaml(path: Path) -> Dict[str, Any]:
    return cast(Dict[str, Any], YAML(typ="safe").load(path.read_text()) or {})


def _discover_example_dirs() -> List[Path]:
    examples_dir = PROJECT_ROOT / "example-answers"
    if not examples_dir.is_dir():
        return []

    example_dirs: List[Path] = []
    for answers_dir in examples_dir.iterdir():
        if not answers_dir.is_dir():
            continue
        pkg = answers_dir / "package.yml"
        module = answers_dir / "module.yml"
        if pkg.exists() and module.exists():
            example_dirs.append(answers_dir)
    return sorted(example_dirs)


EXAMPLE_DIRS: List[Path | None] = _discover_example_dirs() or [None]


def _example_id(example_dir: Path | None) -> str:
    return "no-example-answers" if example_dir is None else example_dir.name


class _LazyExamples:
    def __iter__(self):
        for example_dir in _discover_example_dirs():
            pkg = example_dir / "package.yml"
            module_yaml = example_dir / "module.yml"
            try:
                yield Example(
                    name=example_dir.name,
                    package_answers=_read_yaml(pkg),
                    module_answers=_read_yaml(module_yaml),
                )
            except (FileNotFoundError, OSError, ValueError, TypeError) as exc:
                pytest.fail(
                    f"Failed to load example answers in {example_dir}: {exc}",
                    pytrace=False,
                )


EXAMPLES = _LazyExamples()


# ─────────────────────────────────────────────────────────────────────────────
# Fixture
# ─────────────────────────────────────────────────────────────────────────────


@pytest.fixture(params=EXAMPLE_DIRS, ids=_example_id)
def rendered(request):
    """Render an example and yield (project_dir, example_name)."""
    example_dir: Path | None = request.param

    if example_dir is None:
        pytest.fail(
            "No examples found under `example-answers/` - ensure each example has both "
            "`package.yml` and `module.yml`.",
            pytrace=False,
        )

    pkg = example_dir / "package.yml"
    module_yaml = example_dir / "module.yml"

    try:
        example = Example(
            name=example_dir.name,
            package_answers=_read_yaml(pkg),
            module_answers=_read_yaml(module_yaml),
        )
    except (FileNotFoundError, OSError, ValueError, TypeError) as exc:
        pytest.fail(
            f"Failed to load example answers in {example_dir}: {exc}",
            pytrace=False,
        )

    tmp_root = Path(tempfile.mkdtemp(prefix=f"copie_{example.name}_"))
    config_file = make_copier_config(tmp_root)

    # Package template (parent)
    pkg_dir = tmp_root / "package"
    pkg_dir.mkdir()
    pkg_copie = new_copie(
        template_dir=TEMPLATE_PACKAGE_DIR,
        test_dir=pkg_dir,
        config_file=config_file,
    )

    # Run the package template with output control
    # to avoid cluttering the test output with copier's own logs.
    # This is especially useful when running tests with `-v` or `-vv`.
    pkg_result = run_copie_with_output_control(
        request.config, pkg_copie, example.package_answers
    )

    # Smoke test the package template
    if pkg_result.exit_code or pkg_result.exception:
        pytest.fail(
            f"Package template failed for {example.name}: {pkg_result.exception}"
        )

    # Module template (child)
    module_dir = tmp_root / "module"
    module_dir.mkdir()
    module_copie = new_copie(
        template_dir=TEMPLATE_MODULE_DIR,
        test_dir=module_dir,
        config_file=config_file,
        parent_result=pkg_result,
    )

    # Run the module template with output control
    # to avoid cluttering the test output with copier's own logs.
    # This is especially useful when running tests with `-v` or `-vv`.
    module_result = run_copie_with_output_control(
        request.config, module_copie, example.module_answers
    )

    # Smoke test the module template
    if module_result.exit_code or module_result.exception:
        pytest.fail(
            f"Module template failed for {example.name}: {module_result.exception}"
        )

    logger.debug(f"Rendered '{example.name}' → {module_result.project_dir}")
    return module_result.project_dir, example.name
