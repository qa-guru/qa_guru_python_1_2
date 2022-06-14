import pytest

firefox_mark = pytest.mark.firefox()


@pytest.fixture()
def driver():
    pass


@pytest.fixture()
def config(driver):
    pass


@pytest.fixture()
def firefox(config):
    return ""


@pytest.fixture()
def chrome():
    return ""


@pytest.fixture()
def chrome_mobile():
    return ""
