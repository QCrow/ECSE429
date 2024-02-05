import requests

BASE_URL = "http://localhost:4567"


def test_create_project():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Project"


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
    response = requests.post(
        f"{BASE_URL}/projects/{project_id}", json={"title": "Amended Project"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Amended Project"


def test_amend_project_with_put():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}", json={"title": "Amended Project"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Amended Project"


def test_get_project_by_id():
    response = requests.post(f"{BASE_URL}/projects", json={"title": "Test Project"})
    assert response.status_code == 201
    project_id = response.json()["id"]
    response = requests.get(f"{BASE_URL}/projects/{project_id}")
    assert response.status_code == 200
    assert response.json()["projects"][0]["title"] == "Test Project"


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

    create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert create_response.status_code == 201
    todo_id = create_response.json().get("id")

    response = requests.post(f"{BASE_URL}/projects/{1}/tasks", json={"id": todo_id})
    assert response.status_code == 201


def test_get_project_todos_relationship():
    response = requests.get(f"{BASE_URL}/projects/{1}/tasks")
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json()["todos"], list)


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

    response = requests.post(f"{BASE_URL}/projects/{1}/tasks", json={"id": todo_id})
    assert response.status_code == 201
    response = requests.delete(f"{BASE_URL}/projects/{1}/tasks/{todo_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/projects/{1}/tasks")
    assert todo_id not in [todo["id"] for todo in response.json()["todos"]]


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

    response = requests.post(
        f"{BASE_URL}/projects/{1}/categories", json={"id": category_id}
    )
    assert response.status_code == 201


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

    response = requests.post(
        f"{BASE_URL}/projects/{1}/categories", json={"id": category_id}
    )
    assert response.status_code == 201
    response = requests.delete(f"{BASE_URL}/projects/{1}/categories/{category_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/projects/{1}/categories")
    assert category_id not in [
        category["id"] for category in response.json()["categories"]
    ]


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
    # Using a very high ID number to ensure the project does not exist
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
    # Assuming 1 is a valid project ID. Replace with a valid one if needed.
    response = requests.get(f"{BASE_URL}/projects/1/tasks/999999")
    assert response.status_code == 404


def test_create_project_with_invalid_data():
    # Attempt to create a project with invalid data (empty title)
    response = requests.post(f"{BASE_URL}/projects", json={})
    assert response.status_code == 400


#! Wrong error code
def test_create_invalid_project_todos_relationship_expected():
    # Assume the project ID 999999 does not exist
    non_existent_project_id = 999999
    response = requests.post(
        f"{BASE_URL}/projects/{non_existent_project_id}/tasks", json={"id": 1}
    )
    assert response.status_code == 400


def test_create_invalid_project_todos_relationship_actual():
    # Assume the project ID 999999 does not exist
    non_existent_project_id = 999999
    response = requests.post(
        f"{BASE_URL}/projects/{non_existent_project_id}/tasks", json={"id": 1}
    )
    assert response.status_code == 404
