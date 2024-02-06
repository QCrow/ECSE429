import requests

BASE_URL = "http://localhost:4567"


def test_create_project():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Project"
    assert response.json()["description"] == ""
    assert response.json()["completed"] == "false"
    assert response.json()["active"] == "false"

    response = requests.delete(f"{BASE_URL}/projects/{response.json()['id']}")
    assert response.status_code == 200


def test_get_all_projects():
    response = requests.get(f"{BASE_URL}/projects")
    assert response.status_code == 200
    assert isinstance(response.json()["projects"], list)


def test_get_all_project_headers():
    response = requests.head(f"{BASE_URL}/projects")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_project_endpoint_options():
    response = requests.options(f"{BASE_URL}/projects")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_amend_project_with_post():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert response.status_code == 201
    todo_id = response.json().get("id")

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/tasks", json={"id": todo_id}
    )
    assert response.status_code == 201

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}", json={"title": "Amended Project"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Amended Project"
    assert response.json()["description"] == ""
    assert response.json()["completed"] == "false"
    assert response.json()["active"] == "false"
    assert response.json()["tasks"][0]["id"] == todo_id

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200


def test_amend_project_with_put_expected():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert response.status_code == 201
    todo_id = response.json().get("id")

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/tasks", json={"id": todo_id}
    )
    assert response.status_code == 201

    response = requests.put(
        f"{BASE_URL}/projects/{project_id}", json={"title": "Amended Project"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Amended Project"
    assert response.json()["description"] == ""
    assert response.json()["completed"] == "false"
    assert response.json()["active"] == "false"
    assert response.json()["tasks"][0]["id"] == todo_id

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200


def test_amend_project_with_put_actual():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert response.status_code == 201
    todo_id = response.json().get("id")

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/tasks", json={"id": todo_id}
    )
    assert response.status_code == 201

    response = requests.put(
        f"{BASE_URL}/projects/{project_id}", json={"title": "Amended Project"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Amended Project"
    assert response.json()["description"] == ""
    assert response.json()["completed"] == "false"
    assert response.json()["active"] == "false"

    assert "tasks" not in response.json()

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200


def test_get_project_by_id():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]
    response = requests.get(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    assert response.json()["projects"][0]["title"] == "Test Project"


def test_get_project_invalid_id():
    response = requests.get(f"{BASE_URL}/projects/invalid_id")
    assert response.status_code == 404


def test_get_project_header_by_id():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]
    response = requests.head(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_delete_project_by_id():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]
    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 404


def test_double_delete_project_by_id():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 404


def test_get_project_id_endpoint_options():
    response = requests.options(f"{BASE_URL}/projects/1")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST, PUT, DELETE"


def test_create_project_todos_relationship():
    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert create_response.status_code == 201
    todo_id = create_response.json().get("id")

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/tasks", json={"id": todo_id}
    )
    assert response.status_code == 201

    response = requests.delete(f"{BASE_URL}/projects/{project_id}/tasks/{todo_id}")
    assert response.status_code == 200

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200


def test_get_project_todos_relationship():
    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert create_response.status_code == 201
    todo_id = create_response.json().get("id")

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/tasks", json={"id": todo_id}
    )
    assert response.status_code == 201

    response = requests.get(f"{BASE_URL}/projects/{project_id}/tasks")
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json()["todos"], list)
    assert response.json()["todos"][0]["id"] == todo_id

    response = requests.delete(f"{BASE_URL}/projects/{project_id}/tasks/{todo_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 200


def test_get_project_todos_relationship_invalid_id_expected():
    response = requests.get(f"{BASE_URL}/projects/invalid_id/tasks")
    assert response.status_code == 404


def test_get_project_todos_relationship_invalid_id_actual():
    response = requests.get(f"{BASE_URL}/projects/invalid_id/tasks")
    assert response.status_code == 200


def test_get_project_todos_relationship_headers():
    response = requests.head(f"{BASE_URL}/projects/{1}/tasks")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_project_todos_relationship_options():
    response = requests.options(f"{BASE_URL}/projects/{1}/tasks")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_delete_project_todos_relationship():
    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert create_response.status_code == 201
    todo_id = create_response.json().get("id")

    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/tasks", json={"id": todo_id}
    )
    assert response.status_code == 201
    response = requests.delete(f"{BASE_URL}/projects/{project_id}/tasks/{todo_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/projects/{project_id}/tasks")
    assert todo_id not in [todo["id"] for todo in response.json()["todos"]]


def test_delete_project_todos_relationship_invalid_id():
    response = requests.delete(f"{BASE_URL}/projects/1/tasks/invalid_id")
    assert response.status_code == 404


def test_options_on_project_todos_relationship():
    response = requests.options(f"{BASE_URL}/projects/1/tasks/1")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"


def test_create_project_catergories_relationship():
    category_data = {
        "title": "Test Category",
        "description": "Simple test category",
    }

    create_response = requests.post(f"{BASE_URL}/categories", json=category_data)
    assert create_response.status_code == 201
    category_id = create_response.json().get("id")

    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/categories", json={"id": category_id}
    )
    assert response.status_code == 201

    response = requests.delete(
        f"{BASE_URL}/projects/{project_id}/categories/{category_id}"
    )
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/categories/{category_id}")
    assert response.status_code == 200


def test_get_project_categories_relationship():
    response = requests.get(f"{BASE_URL}/projects/{1}/categories")
    assert response.status_code == 200
    assert isinstance(response.json()["categories"], list)


def test_get_project_categories_relationship_headers():
    response = requests.head(f"{BASE_URL}/projects/{1}/categories")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_project_categories_relationship_options():
    response = requests.options(f"{BASE_URL}/projects/{1}/categories")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, GET, HEAD, POST"


def test_delete_project_categories_relationship():
    category_data = {
        "title": "Test Category",
        "description": "Simple test category",
    }

    create_response = requests.post(f"{BASE_URL}/categories", json=category_data)
    assert create_response.status_code == 201
    category_id = create_response.json().get("id")

    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.post(
        f"{BASE_URL}/projects/{project_id}/categories", json={"id": category_id}
    )
    assert response.status_code == 201
    response = requests.delete(
        f"{BASE_URL}/projects/{project_id}/categories/{category_id}"
    )
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/projects/{project_id}/categories")
    assert category_id not in [
        category["id"] for category in response.json()["categories"]
    ]
    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    response = requests.delete(f"{BASE_URL}/categories/{category_id}")
    assert response.status_code == 200


def test_options_on_project_categories_id_relationship():
    response = requests.options(f"{BASE_URL}/projects/1/categories/1")
    assert response.status_code == 200
    assert response.headers["Allow"] == "OPTIONS, DELETE"


def test_put_on_projects_collection():
    response = requests.put(f"{BASE_URL}/projects")
    assert response.status_code == 405


def test_delete_on_projects_collection():
    response = requests.delete(f"{BASE_URL}/projects")
    assert response.status_code == 405


def test_patch_on_specific_project():
    response = requests.patch(f"{BASE_URL}/projects/1")
    assert response.status_code == 405


def test_get_nonexistent_project():
    response = requests.get(f"{BASE_URL}/projects/999999")
    assert response.status_code == 404


def test_update_nonexistent_project():
    response = requests.put(
        f"{BASE_URL}/projects/999999", json={"title": "Ghost Project"}
    )
    assert response.status_code == 404


def test_delete_nonexistent_project():
    response = requests.delete(f"{BASE_URL}/projects/999999")
    assert response.status_code == 404


def test_get_nonexistent_todo_in_project():
    response = requests.get(f"{BASE_URL}/projects/1/tasks/999999")
    assert response.status_code == 404


def test_create_project_with_empty_data():
    response = requests.post(f"{BASE_URL}/projects", json={})
    assert response.status_code == 201
    project_id = response.json()["id"]

    response = requests.delete(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200


def test_create_invalid_project_todos_relationship_expected():
    non_existent_project_id = 999999
    response = requests.post(
        f"{BASE_URL}/projects/{non_existent_project_id}/tasks", json={"id": 1}
    )
    assert response.status_code == 400


def test_create_invalid_project_todos_relationship_actual():
    non_existent_project_id = 999999
    response = requests.post(
        f"{BASE_URL}/projects/{non_existent_project_id}/tasks", json={"id": 1}
    )
    assert response.status_code == 404


def test_not_implemented_get_project_todos_id_expected():
    response = requests.get(f"{BASE_URL}/projects/1/tasks/1")
    assert response.status_code == 405


def test_not_implemented_get_project_todos_id_actual():
    response = requests.get(f"{BASE_URL}/projects/1/tasks/1")
    assert response.status_code == 404


def test_not_implemented_post_project_todos_id_expected():
    response = requests.post(f"{BASE_URL}/projects/1/tasks/1")
    assert response.status_code == 405


def test_not_implemented_post_project_todos_id_actual():
    response = requests.post(f"{BASE_URL}/projects/1/tasks/1")
    assert response.status_code == 404
