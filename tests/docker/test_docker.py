import pytest

EXPECTED_USER_NAME: str = "oltho"
EXPECTED_UID: int = 2001
EXPECTED_USER_GROUP: str = "oltho"
EXPECTED_GID: int = 2001


def test_service_account(host):
    user = host.user()
    assert user.name == EXPECTED_USER_NAME
    assert user.uid == EXPECTED_UID
    assert user.group == EXPECTED_USER_GROUP
    assert user.gid == EXPECTED_GID
