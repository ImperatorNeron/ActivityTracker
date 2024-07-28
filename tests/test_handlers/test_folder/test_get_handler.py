def test_get_user_folders(client, auth_headers_for_user):
    response = client.get("/api/v1/folders/", headers=auth_headers_for_user)
    assert response.status_code == 200
    assert isinstance(response.json(), list)