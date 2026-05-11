"""Validate snakefmt configuration is sourced from pyproject.toml."""


def test_template_uses_pyproject_for_snakefmt(rendered):
    project_dir, _ = rendered

    pyproject = (project_dir / "pyproject.toml").read_text(encoding="utf-8")
    assert "[tool.snakefmt]" in pyproject
    assert "line_length = 79" in pyproject
    assert "include = '\\.smk$|^Snakefile$'" in pyproject
    assert not (project_dir / "snakefmt.toml").exists()
