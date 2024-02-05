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

    def test_create_todo_with_malformed_data(self):
        todo_data = {
            "title": "Test Todo",
            "doneStatus": False,
            "description": "Simple test todo",
            "extra": "extra data"
        }

        create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
        assert create_response.status_code == 400

    def test_get_all_todos(self):
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

    def test_patch_all_todos(self):
        patch_response = requests.patch(f"{BASE_URL}/todos")
        # this should fail as the method is not allowed
        assert patch_response.status_code == 405

    def test_get_todo_by_id(self):
        todo_id = self.test_create_todo()
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}")
        assert get_response.status_code == 200 and (get_response.json()["todos"][0]["id"]) == todo_id

    def test_update_todo_by_id(self):
        todo_id = 1
        todo_data = {
            "title": "Updated Todo",
            "doneStatus": True,
            "description": "Updated test todo",
        }
        update_response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=todo_data)
        assert update_response.status_code == 200 and update_response.json()["id"] == "1"

    def test_create_todo_with_id(self):
        todo_id = 1
        todo_data = {
            "title": "Test Todo",
            "doneStatus": False,
            "description": "Simple test todo",
        }

        create_response = requests.post(f"{BASE_URL}/todos/{todo_id}", json=todo_data)
        assert create_response.status_code == 200 and create_response.json()["id"] == "1"

    def test_delete_todo_by_id(self):
        todo_data = {
            "title": "Test Todo",
            "doneStatus": False,
            "description": "Simple test todo",
        }

        create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)
        assert create_response.status_code == 201
        todo_id = create_response.json().get("id")
        
        todo_data = {
            "title": "Test Todo",
            "doneStatus": False,
            "description": "Simple test todo",
        }
        requests.post(f"{BASE_URL}/todos/{todo_id}", json=todo_data)
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        assert delete_response.status_code == 200

    def test_delete_inexistent_todo_by_id(self):
        todo_id = 100
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        assert delete_response.status_code == 404

    def test_options_todo_by_id(self):
        todo_id = 1
        options_response = requests.options(f"{BASE_URL}/todos/{todo_id}")
        assert options_response.status_code == 200

    def test_head_todo_by_id(self):
        todo_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}")
        assert head_response.status_code == 200

    def test_patch_todo_by_id(self):
        todo_id = 1
        patch_response = requests.patch(f"{BASE_URL}/todos/{todo_id}")
        # this should fail as the method is not allowed
        assert patch_response.status_code == 405

    #categories
    def test_get_categories_by_todo_id(self):
        todo_id = 1
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}/categories")
        assert get_response.status_code == 200

    def test_create_categories_by_todo_id(self):
        todo_id = 1
        category_data = {
            "id": "1",
            "title": "categories_test",
            "description": "test of category 1",
        }
        create_response = requests.post(f"{BASE_URL}/todos/{todo_id}/categories", json=category_data)
        assert create_response.status_code == 201

    def test_update_categories_by_todo_id(self):
        todo_id = 1
        category_id = 1
        category_data = {
            "id": "1",
            "title": "categories_test",
            "description": "test of category 1",
        }
        update_response = requests.put(f"{BASE_URL}/todos/{todo_id}/categories", json=category_data)
        # this should fail as the method is not allowed
        assert update_response.status_code == 405

    def test_delete_categories_by_todo_id(self):
        todo_id = 1
        category_id = 1
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}/categories")
        # this should fail as the method is not allowed
        assert delete_response.status_code == 405

    def test_options_categories_by_todo_id(self):
        todo_id = 1
        options_response = requests.options(f"{BASE_URL}/todos/{todo_id}/categories")
        assert options_response.status_code == 200

    def test_head_categories_by_todo_id(self):
        todo_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}/categories")
        assert head_response.status_code == 200

    def test_patch_categories_by_todo_id(self):
        todo_id = 1
        patch_response = requests.patch(f"{BASE_URL}/todos/{todo_id}/categories")
        # this should fail as the method is not allowed
        assert patch_response.status_code == 405
    
    #tasksof
    def test_get_tasksof_by_todo_id(self):
        todo_id = 1
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}/tasksof")
        assert get_response.status_code == 200
    
    def test_create_tasksof_by_todo_id(self):
        todo_id = 1
        tasksof_data = {
            "id": "1",
            "title": "tasksof_test",
            "description": "test of tasksof 1",
        }
        create_response = requests.post(f"{BASE_URL}/todos/{todo_id}/tasksof", json=tasksof_data)
        assert create_response.status_code == 201

    def test_update_tasksof_by_todo_id(self):
        todo_id = 1
        tasksof_id = 1
        tasksof_data = {
            "id": "1",
            "title": "tasksof_test",
            "description": "test of tasksof 1",
        }
        update_response = requests.put(f"{BASE_URL}/todos/{todo_id}/tasksof", json=tasksof_data)
        # this should fail as the method is not allowed
        assert update_response.status_code == 405

    def test_delete_tasksof_by_todo_id(self):
        todo_id = 1
        tasksof_id = 1
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}/tasksof")
        # this should fail as the method is not allowed
        assert delete_response.status_code == 405

    def test_options_tasksof_by_todo_id(self):
        todo_id = 1
        options_response = requests.options(f"{BASE_URL}/todos/{todo_id}/tasksof")
        assert options_response.status_code == 200

    def test_head_tasksof_by_todo_id(self):
        todo_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}/tasksof")
        assert head_response.status_code == 200

    def test_patch_tasksof_by_todo_id(self):
        todo_id = 1
        patch_response = requests.patch(f"{BASE_URL}/todos/{todo_id}/tasksof")
        # this should fail as the method is not allowed
        assert patch_response.status_code == 405

    #categories by id
    def test_get_categories_by_todo_id_and_category_id_expected_behavior(self):
        todo_id = 1
        category_id = 1
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert get_response.status_code == 405

    def test_get_categories_by_todo_id_and_category_id_actual_behavior(self):
        todo_id = 1
        category_id = 1
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert get_response.status_code == 404

    def test_update_categories_by_todo_id_and_category_id(self):
        todo_id = 1
        category_id = 1
        category_data = {
            "id": "1",
            "title": "categories_test",
            "description": "test of category 1",
        }
        update_response = requests.put(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}", json=category_data)
        assert update_response.status_code == 405

    def test_delete_categories_by_todo_id_and_category_id_expected_behavior(self):
        todo_id = 1
        category_id = 1
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert delete_response.status_code == 405

    def test_delete_categories_by_todo_id_and_category_id_actual_behavior(self):
        todo_id = 1
        category_id = 1
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert delete_response.status_code == 404

    def test_options_categories_by_todo_id_and_category_id(self):
        todo_id = 1
        category_id = 1
        options_response = requests.options(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert options_response.status_code == 200

    def test_head_categories_by_todo_id_and_category_id_expected_behavior(self):
        todo_id = 1
        category_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert head_response.status_code == 405

    def test_head_categories_by_todo_id_and_category_id_actual_behavior(self):
        todo_id = 1
        category_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert head_response.status_code == 404

    def test_patch_categories_by_todo_id_and_category_id(self):
        todo_id = 1
        category_id = 1
        patch_response = requests.patch(f"{BASE_URL}/todos/{todo_id}/categories/{category_id}")
        assert patch_response.status_code == 405

    #tasksof by id
    def test_get_tasksof_by_todo_id_and_tasksof_id_expected_behavior(self):
        todo_id = 1
        tasksof_id = 1
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert get_response.status_code == 405

    def test_get_tasksof_by_todo_id_and_tasksof_id_actual_behavior(self):
        todo_id = 1
        tasksof_id = 1
        get_response = requests.get(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert get_response.status_code == 404

    def test_update_tasksof_by_todo_id_and_tasksof_id(self):
        todo_id = 1
        tasksof_id = 1
        tasksof_data = {
            "id": "1",
            "title": "tasksof_test",
            "description": "test of tasksof 1",
        }
        update_response = requests.put(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}", json=tasksof_data)
        assert update_response.status_code == 405

    def test_delete_tasksof_by_todo_id_and_tasksof_id_expected_behavior(self):
        todo_id = 1
        tasksof_id = 1
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert delete_response.status_code == 405

    def test_delete_tasksof_by_todo_id_and_tasksof_id_actual_behavior(self):
        todo_id = 1
        tasksof_id = 1
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert delete_response.status_code == 404

    def test_options_tasksof_by_todo_id_and_tasksof_id(self):
        todo_id = 1
        tasksof_id = 1
        options_response = requests.options(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert options_response.status_code == 200

    def test_head_tasksof_by_todo_id_and_tasksof_id_expected_behavior(self):
        todo_id = 1
        tasksof_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert head_response.status_code == 405

    def test_head_tasksof_by_todo_id_and_tasksof_id_actual_behavior(self):
        todo_id = 1
        tasksof_id = 1
        head_response = requests.head(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert head_response.status_code == 404

    def test_patch_tasksof_by_todo_id_and_tasksof_id(self):
        todo_id = 1
        tasksof_id = 1
        patch_response = requests.patch(f"{BASE_URL}/todos/{todo_id}/tasksof/{tasksof_id}")
        assert patch_response.status_code == 405
    
