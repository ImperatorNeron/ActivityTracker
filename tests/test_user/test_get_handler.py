def test_get_me(client, auth_headers_for_user):
    response = client.get("/api/v1/users/me", headers=auth_headers_for_user)
    assert response.status_code == 200
