def test_create_and_delete_folder(client, auth_headers_for_user):
    headers = {
        "accept": "application/json",
        **auth_headers_for_user,
    }

    folder_data = {
        "title": "Test folder",
        "description": "my test folder",
        "tasks_quantity": 0,
    }

    response = client.post("/api/v1/folders/", json=folder_data, headers=headers)
    assert response.status_code == 200

    folder_id = response.json()["id"]

    response = client.get(f"/api/v1/folders/{folder_id}", headers=headers)

    assert response.status_code == 200
    assert response.json()["description"] == "my test folder"

    response = client.delete(
        f"/api/v1/folders/delete/{folder_id}",
        headers=headers,
    )
    assert response.status_code == 200
