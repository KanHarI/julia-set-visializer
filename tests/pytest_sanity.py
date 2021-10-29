import pytest


def test_sanity_passes() -> None:
    assert 0 == 0


@pytest.mark.xfail
def test_sanity_fails() -> None:
    x = [0]
    assert len(x) > 2
