import pytest

@pytest.mark.parametrize(
    ("auth_required_disabled", "status", "code"),
    [
        (True, 200, 100)
    ]
)
def test_get_users(client, auth_required_disabled, status, code):
    result = client.get(
        "/api/v1/users",
        headers={
            "X-Disable-AuthRequired": "YES" if auth_required_disabled else "NO"
        }
    )
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code

@pytest.mark.parametrize(
    ("auth_required_disabled", "user_id", "status", "code"),
    [
        (True, "notfound", 404, 103)
    ]
)
def test_get_user(client, auth_required_disabled, user_id, status, code):
    result = client.get(
        f"/api/v1/users/{user_id}",
        headers={
            "X-Disable-AuthRequired": "YES" if auth_required_disabled else "NO"
        }
    )
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code
