def test_get_me(client, auth_headers_for_user):
    response = client.get("/api/v1/users/me", headers=auth_headers_for_user)
    assert response.status_code == 200


def test_get_me_two_users(
    client,
    auth_headers_for_user,
    auth_headers_for_user_2,
):
    response_user_1 = client.get("/api/v1/users/me", headers=auth_headers_for_user)
    response_user_2 = client.get("/api/v1/users/me", headers=auth_headers_for_user_2)

    assert response_user_1.status_code == 200
    assert response_user_2.status_code == 200
