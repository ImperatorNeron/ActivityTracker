def get_task_test_data(**kwargs):
    return {"title": "Test task", "start_value": 10, "goal_value": 100, **kwargs}


def get_folder_test_data():
    return {
        "title": "Test folder for folder",
        "description": "my test folder",
        "tasks_quantity": 0,
    }


def test_create_task_in_nonexistent_folder(client, auth_headers_for_user):
    headers = {"accept": "application/json", **auth_headers_for_user}
    response = client.post(
        "/api/v1/tasks/",
        json=get_task_test_data(folder_id=111),
        headers=headers,
    )
    assert response.status_code == 404


def test_create_task_in_another_user_folder(
    client,
    auth_headers_for_user,
    auth_headers_for_user_2,
):
    response = client.post(
        "/api/v1/folders/",
        json=get_folder_test_data(),
        headers={"accept": "application/json", **auth_headers_for_user_2},
    )
    assert response.status_code == 200

    another_user_folder_id = response.json()["id"]
    response = client.post(
        "/api/v1/tasks/",
        json=get_task_test_data(folder_id=another_user_folder_id),
        headers={"accept": "application/json", **auth_headers_for_user},
    )
    assert response.status_code == 404

    response = client.delete(
        f"/api/v1/folders/delete/{another_user_folder_id}",
        headers={"accept": "application/json", **auth_headers_for_user_2},
    )
    assert response.status_code == 200
