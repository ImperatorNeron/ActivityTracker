def test_create_and_get_and_delete_task_without_folder(
    client,
    auth_headers_for_user,
):
    headers = {
        "accept": "application/json",
        **auth_headers_for_user,
    }

    task_data = {
        "title": "Test task",
        "start_value": 0,
        "goal_value": 100,
    }

    response = client.post(
        "/api/v1/tasks/",
        json=task_data,
        headers=headers
    )

    assert response.status_code == 200

    task_id = response.json()["id"]

    response = client.get(f"/api/v1/tasks/{task_id}", headers=headers)

    assert response.status_code == 200

    response = client.delete(f"/api/v1/tasks/delete/{task_id}", headers=headers)

    assert response.status_code == 200
