
import pytest


@pytest.fixture()
def before_each(request):
    print("Called before each test " + request.node.name)


@pytest.fixture(scope='module', autouse=True)
def init_browser(request):
    print("Called before all tests " + request.node.name)


@pytest.fixture()
def message():
    return "This is message"


@pytest.mark.firefox
@pytest.fixture()
def client():
    print(123231)
    yield
    print("А теперь удаляем клиента")


def test_first(before_each):
    assert 1 == 1


def test_second(before_each):
    assert 1 == 2, "Единица не должна быть равна двойке!"


class TestOther:
    def test_message(self, message, chrome_mobile):
        print(message)
        assert "message" in message

    def test_client(self, client):
        assert client == 321
