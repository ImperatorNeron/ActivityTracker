def get_task_test_data(**kwargs):
    return {"title": "Test task 2", "start_value": 10, "goal_value": 100, **kwargs}


def get_folder_test_data():
    return {
        "title": "Test folder",
        "description": "my test folder",
        "tasks_quantity": 0,
    }


def test_create_and_get_and_delete_task_without_folder(
    client,
    auth_headers_for_user,
):
    headers = {"accept": "application/json", **auth_headers_for_user}

    response = client.post("/api/v1/tasks/", json=get_task_test_data(), headers=headers)
    assert response.status_code == 200

    task_id = response.json()["id"]
    response = client.get(f"/api/v1/tasks/{task_id}", headers=headers)
    assert response.status_code == 200

    response = client.delete(f"/api/v1/tasks/delete/{task_id}", headers=headers)
    assert response.status_code == 200


def test_create_and_get_and_delete_task_with_folder(
    client,
    auth_headers_for_user,
):
    headers = {"accept": "application/json", **auth_headers_for_user}

    response = client.post(
        "/api/v1/folders/", json=get_folder_test_data(), headers=headers
    )
    assert response.status_code == 200

    folder_id = response.json()["id"]
    response = client.post(
        "/api/v1/tasks/",
        json=get_task_test_data(folder_id=folder_id),
        headers=headers,
    )
    assert response.status_code == 200

    task_id = response.json()['id']
    response = client.get(f"/api/v1/tasks/{task_id}", headers=headers)
    assert response.status_code == 200

    response = client.delete(f"/api/v1/tasks/delete/{task_id}", headers=headers)
    assert response.status_code == 200

    response = client.delete(
        f"/api/v1/folders/delete/{folder_id}",
        headers=headers,
    )
    assert response.status_code == 200
