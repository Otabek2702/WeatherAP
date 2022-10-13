import pytest
from app import app0


@pytest.fixture()
def app():
    app = app0
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_home_page(client):
    response = client.get("/")
    assert b"<h2 class=\"section-title\">Live cameras</h2>" in response.data


def test_contact_page(client):
    response = client.get("/contact")
    assert b"<h2 class=\"section-title\">Contact us</h2>" in response.data


def test_news_page(client):
    response = client.get("/news")
    assert b"<h2 class=\"entry-title\">Nemo enim ipsam voluptatem quia voluptas</h2>" in response.data


def test_live_cameras(client):
    response = client.get("/live-cameras")
    assert b"<label for=\"\">Country</label>" in response.data


def test_apiv0_without_login(client):
    response = client.get("/apiv0/daily_weather")
    assert b'{ "msg": "Missing Authorization Header"}' in response.data
