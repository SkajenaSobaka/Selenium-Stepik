import pytest


def valid_config():
    pass


@pytest.mark.xfail(strict=True)
def test_succeed():
    # if not valid_config():
    #     pytest.xfail("failing configuration (but should work)")
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False