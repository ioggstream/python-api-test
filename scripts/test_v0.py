import pytest
from pathlib import Path
v0_files = """
README.md
LICENSE
.yamllint
.github/workflows/lint.yml
.github/workflows/yamllint.yml
.github/ISSUE_TEMPLATE/custom.md
.github/pull_request_template.md""".split()


@pytest.mark.parametrize("fpath", v0_files)
def test_v0(fpath):
    assert Path(fpath).exists()





