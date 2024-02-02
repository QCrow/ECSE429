import requests

BASE_URL = "http://localhost:4567"


def test_create_and_fetch_todo():
    # Step 1: Create a new todo
    todo_data = {
        "title": "Test Todo",
        "doneStatus": False,
        "description": "Simple test todo",
    }

    create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    assert create_response.status_code == 201
    todo_id = create_response.json().get("id")

    # Step 2: Fetch the newly created todo to verify it exists
    fetch_response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    assert fetch_response.status_code == 200
    fetched_todo = fetch_response.json().get("todos")[0]
    assert fetched_todo.get("title") == todo_data["title"]
    assert fetched_todo.get("description") == todo_data["description"]

    # Step 3: Delete the created todo to restore the state
    delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert delete_response.status_code == 200
