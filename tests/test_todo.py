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

    def test_update_all_todos(self):
        todo_id = self.test_create_todo()
        todo_data = {
            "title": "Updated Todo",
            "doneStatus": True,
            "description": "Updated test todo",
        }
        update_response = requests.put(f"{BASE_URL}/todos", json=todo_data)
        # this should fail as the method is not allowed
        assert update_response.status_code == 405

    def test_delete_all_todos(self):
        delete_response = requests.delete(f"{BASE_URL}/todos")
        # this should fail as the method is not allowed
        assert delete_response.status_code == 405

    def test_options_all_todos(self):
        options_response = requests.options(f"{BASE_URL}/todos")
        assert options_response.status_code == 200

    def test_head_all_todos(self):
        head_response = requests.head(f"{BASE_URL}/todos")
        assert head_response.status_code == 200