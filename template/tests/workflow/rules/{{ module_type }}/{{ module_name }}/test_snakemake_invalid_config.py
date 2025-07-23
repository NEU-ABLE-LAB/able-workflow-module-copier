"""
Tests for confirming the Snakemake configuration schema
validation fails when the schema is not followed.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from tests.workflow.rules.conftest import _snakemake


# --- Fixtures ---------------------------------------------------------------
@pytest.fixture(autouse=True)
def create_dummy_input_data(
    workspace: Path,
    request: pytest.FixtureRequest,
):
    """Create the expected input files so Snakemake can build the DAG."""

    # Copy the test data for the `all_data` rule
    repo_root = request.config.rootdir
    shutil.copytree(repo_root / "data/tests", workspace / "data")


@pytest.fixture(autouse=True)
def create_invalid_config(
    workspace: Path,
):
    """Create an invalid config file to test schema validation."""

    # Create an invalid config file that does not follow the schema
    invalid_config = {
        "TOX": "tox",
        "WORKFLOW": "workflow",
        # Missing required fields or incorrect types can be added here
    }

    (workspace / "config" / "config.yaml").write_text(str(invalid_config))


# --- Tests ------------------------------------------------------------------
def test_snakemake_all_data_invalid_config(workspace: Path) -> None:
    """
    The workflow must abort when the config violates the schema.
    We consider the test *passed* only if Snakemake exits with a
    CalledProcessError whose stderr contains the schema-validation
    message.
    """
    with pytest.raises(subprocess.CalledProcessError) as excinfo:
        _snakemake(workspace, ["--dry-run", "all_data"])

    # Narrow assertion: make sure we failed *because* of schema validation
    stderr = excinfo.value.stderr.decode()
    assert "ValidationError" in stderr or "Failed validating" in stderr
