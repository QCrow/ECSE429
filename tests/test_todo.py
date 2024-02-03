import requests

BASE_URL = "http://localhost:4567"

class TestClass:

    def test_create_todo(self):
        todo_data = {
            "title": "Test Todo",
            "doneStatus": False,
            "description": "Simple test todo",
        }

        create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
        assert create_response.status_code == 201
        todo_id = create_response.json().get("id")
        return todo_id

    def get_all_todos(self):
        get_response = requests.get(f"{BASE_URL}/todos")
        assert get_response.status_code == 200
        return get_response.json()