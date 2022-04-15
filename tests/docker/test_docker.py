import pytest

# can have hard coded expected value
EXPECTED_USER_NAME: str = "oltho"
EXPECTED_UID: int = 2001
EXPECTED_USER_GROUP: str = "oltho"
EXPECTED_GID: int = 2001

@pytest.mark.docker
def test_service_account(host):
    user = host.user()
    assert user.name == EXPECTED_USER_NAME
    assert user.uid == EXPECTED_UID
    assert user.group == EXPECTED_USER_GROUP
    assert user.gid == EXPECTED_GID

@pytest.mark.docker
def test_flask_listenning(host):
    # can fetch dynamic expected value from ENV variable WITHIN container
    env: dict = host.environment()
    expected_listen_host = env.get("FLASK_HOST")
    expected_listen_port = env.get("FLASK_PORT")
    assert host.socket(
        f"tcp://{expected_listen_host}:{expected_listen_port}").is_listening

@pytest.mark.docker
def test_pip(host):
    env: dict = host.environment()
    expected_pip_version = env.get("PIP_VERSION")

    assert expected_pip_version in host.run("pip --version").stdout
