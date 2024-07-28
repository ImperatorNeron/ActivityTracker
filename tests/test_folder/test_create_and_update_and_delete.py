def test_create_and_update_and_delete_folder(client, auth_headers_for_user):
    headers = {
        "accept": "application/json",
        **auth_headers_for_user,
    }

    create_folder_data = {
        "title": "Test folder",
        "tasks_quantity": 0,
    }

    patch_folder_data = {
        "description": "my test folder",
        "tasks_quantity": 5,
    }

    response = client.post(
        "/api/v1/folders/",
        json=create_folder_data,
        headers={"Content-Type": "application/json", **headers},
    )
    assert response.status_code == 200

    folder_id = response.json()["id"]

    response = client.patch(
        f"/api/v1/folders/{folder_id}",
        json=patch_folder_data,
        headers={"Content-Type": "application/json", **headers},
    )

    assert response.status_code == 200
    assert response.json()["tasks_quantity"] == 5
    assert response.json()["description"] == "my test folder"

    response = client.delete(
        f"/api/v1/folders/delete/{folder_id}",
        headers=headers,
    )
    assert response.status_code == 200
