from random import random


def get_task_test_data(**kwargs):
    return {
        "title": f"Test task {random()}",
        "start_value": 10,
        "goal_value": 100,
        **kwargs,
    }


def get_folder_test_data():
    return {
        "title": f"Test folder {random()}",
        "description": "my test folder",
        "tasks_quantity": 0,
    }


def test_patch_task_to_nonexistent_folder(client, auth_headers_for_user):
    headers = {"accept": "application/json", **auth_headers_for_user}
    response = client.post("/api/v1/tasks/", json=get_task_test_data(), headers=headers)
    assert response.status_code == 200
    task_id = response.json()["id"]
    response = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"folder_id": "10000"},
        headers={"Content-Type": "application/json", **headers},
    )
    assert response.status_code == 404
    response = client.delete(f"/api/v1/tasks/delete/{task_id}", headers=headers)
    assert response.status_code == 200


def test_patch_task_to_another_user_folder(
    client,
    auth_headers_for_user,
    auth_headers_for_user_2,
):
    headers = {"accept": "application/json", **auth_headers_for_user}
    response_1 = client.post(
        "/api/v1/tasks/", json=get_task_test_data(), headers=headers
    )
    assert response_1.status_code == 200

    headers_2 = {"accept": "application/json", **auth_headers_for_user_2}
    response_2 = client.post(
        "/api/v1/folders/", json=get_folder_test_data(), headers=headers_2
    )
    assert response_2.status_code == 200

    task_id = response_1.json()["id"]
    another_user_folder_id = response_2.json()["id"]

    response_1 = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"folder_id": another_user_folder_id},
        headers={"Content-Type": "application/json", **headers},
    )
    assert response_1.status_code == 404

    response_1 = client.delete(f"/api/v1/tasks/delete/{task_id}", headers=headers)
    assert response_1.status_code == 200

    response_2 = client.delete(
        f"/api/v1/folders/delete/{another_user_folder_id}",
        headers=headers_2,
    )
    assert response_2.status_code == 200
