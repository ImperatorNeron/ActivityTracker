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
    task_id = response.json()['id']
    response = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"folder_id": "10000"},
        headers={"Content-Type": "application/json", **headers},
    )
    assert response.status_code == 404
    response = client.delete(f"/api/v1/tasks/delete/{task_id}", headers=headers)
    assert response.status_code == 200

