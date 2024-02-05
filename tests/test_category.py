import requests
BASE_URL = "http://localhost:4567"

class TestClass:

    "creat a category"
    def test_create_categories(self):
        categories_data = {
            
            "title": "categories_test",
            "description": "test of category 1"
        }

        create_response = requests.post(f"{BASE_URL}/categories", json=categories_data)
        assert create_response.status_code == 201
        categories_id = create_response.json().get("id")
        return categories_id
    
    
    "creat a todo"
    def test_create_todo(self):
        todo_data = {
            "title": "Todo for category",
            "doneStatus": False,
            "description": "A todo to test the category relationship."
        }
        response = requests.post(f"{BASE_URL}/todos", json=todo_data)
        assert response.status_code == 201
        todo_id = response.json().get("id")
        return todo_id
    
    "end point with category"
    def test_post_an_empty_category(self):
        create_response = requests.post(f"{BASE_URL}/categories")
        assert create_response.status_code == 400, "bad request"


    def test_get_all_categories(self):
      
        get_response = requests.get(f"{BASE_URL}/categories")
        assert get_response.status_code == 200
        categories = get_response.json()
        assert isinstance(categories, dict), "Response should be a dictionary"

    def test_method_not_allowed_on_base_endpoint(self):
        put_response = requests.put(f"{BASE_URL}/categories", json={})
        assert put_response.status_code == 405, "PUT should not be allowed on base /categories"

        delete_response = requests.delete(f"{BASE_URL}/categories")
        assert delete_response.status_code == 405, "DELETE should not be allowed on base /categories"

        patch_response = requests.patch(f"{BASE_URL}/categories")
        assert patch_response.status_code == 405


    def test_options_on_categories(self):
        options_response = requests.options(f"{BASE_URL}/categories")
        assert options_response.status_code == 200

    def test_head_on_categories(self):
        head_response = requests.head(f"{BASE_URL}/categories")
        assert head_response.status_code == 200

    def test_patch_method_not_allowed(self):
        patch_response = requests.patch(f"{BASE_URL}/categories")
        assert patch_response.status_code == 405


    "end point with category_id"
 
    def test_get_specific_category(self):
        category_id = self.test_create_categories()
        response = requests.get(f"{BASE_URL}/{category_id}")
        assert response.status_code == 200

    def test_update_or_put_specific_category(self):
        category_id = self.test_create_categories()
        updated_category_data = {
            "title": "Updated Category Title",
            "description": "Updated category description"
        }
        update_response = requests.put(f"{BASE_URL}/categories/{category_id}", json=updated_category_data)
        assert update_response.status_code == 200

    def test_delete_specific_category(self):
        category_id = self.test_create_categories()
        delete_response = requests.delete(f"{BASE_URL}/categories/{category_id}")
        assert delete_response.status_code == 200
        
    def test_post_specific_category_not_allowed(self):
        category_id = self.test_create_categories()
        data = {"title": "Attempt to Post", "description": "Post Description"}
        response = requests.post(f"{BASE_URL}/{category_id}", json=data)
        assert response.status_code == 404

    def test_options_specific_category(self):
        category_id = self.test_create_categories()
        response = requests.options(f"{BASE_URL}/{category_id}")
        assert response.status_code == 200

    def test_head_specific_category(self):
        category_id = self.test_create_categories()
        response = requests.head(f"{BASE_URL}/{category_id}")
        assert response.status_code == 200

    def test_patch_specific_category_not_allowed(self):
        category_id = self.test_create_categories()
        data = {"title": "Patch testing", "description": "shoulkd not work"}
        response = requests.patch(f"{BASE_URL}/{category_id}", json=data)
        assert response.status_code == 405
        
    "test with /categories/:id/projects"

    def test_get_projects_for_category(self):
        category_id = self.test_create_categories()
        response = requests.get(f"{BASE_URL}/categories/{category_id}/projects")
        assert response.status_code == 200

    def test_method_not_allowed_for_end_point_category_projects(self):
        category_id = self.test_create_categories()
        
        # PUT method
        put_response = requests.put(f"{BASE_URL}/categories/{category_id}/projects")
        assert put_response.status_code == 405

        #DELETE method
        delete_response = requests.delete(f"{BASE_URL}/categories/{category_id}/projects")
        assert delete_response.status_code == 405

        #PATCH method
        patch_response = requests.patch(f"{BASE_URL}/categories/{category_id}/projects")
        assert patch_response.status_code == 405

    def test_options_for_category_projects(self):

        category_id = self.test_create_categories()
        response = requests.options(f"{BASE_URL}/categories/{category_id}/projects")
        assert response.status_code == 200

    def test_head_for_category_projects(self):
      
        category_id = self.test_create_categories()
        response = requests.head(f"{BASE_URL}/categories/{category_id}/projects")
        assert response.status_code == 200
        
        
        
        
    "/categories/:id/projects/:id"
    def test_create_project(self):
        project_data = {
            "title": "Project for Category Relationship",
            "description": "A project to test the relationship with categories."
        }
        response = requests.post(f"{BASE_URL}/projects", json=project_data)
        assert response.status_code == 201
        return response.json().get("id")

    def test_method_restrictions_for_category_project_endpoint(self):
        category_id = self.test_create_categories()
        project_id = self.test_create_project()
        for method in [requests.get, requests.put, requests.post, requests.patch, requests.head]:
            response = method(f"{BASE_URL}/categories/{category_id}/projects/{project_id}")
            assert response.status_code == 405

    def test_options_for_category_project_endpoint(self):
        category_id = self.test_create_categories()
        project_id = self.test_create_project()
        response = requests.options(f"{BASE_URL}/categories/{category_id}/projects/{project_id}")
        assert response.status_code == 200

    def test_delete_category_project_relationship(self):
        category_id = self.test_create_categories()
        project_id = self.test_create_project()
        response = requests.delete(f"{BASE_URL}/categories/{category_id}/projects/{project_id}")
        assert response.status_code in [200, 400, 404]
        
        
        
        "/categories/:id/todos"
    
    def test_get_todos_for_category(self):
        category_id = self.test_create_categories()
        response = requests.get(f"{BASE_URL}/categories/{category_id}/todos")
        assert response.status_code == 200

    def test_options_for_category_todos(self):
        category_id = self.test_create_categories()
        response = requests.options(f"{BASE_URL}/categories/{category_id}/todos")
        assert response.status_code == 200

    def test_head_for_category_todos(self):
        category_id = self.test_create_categories()
        response = requests.head(f"{BASE_URL}/categories/{category_id}/todos")
        assert response.status_code == 200

    def test_method_not_allowed(self):
        category_id = self.test_create_categories()
        for method in [requests.put, requests.delete, requests.patch]:
            response = method(f"{BASE_URL}/categories/{category_id}/todos")
            assert response.status_code == 405

    def test_post_todo_to_category(self):
        category_id = self.test_create_categories()
        todo_id = self.test_create_todo()
        relationship_data = {"id": todo_id}
        response = requests.post(f"{BASE_URL}/categories/{category_id}/todos", json=relationship_data)
        assert response.status_code in [201, 400]
        
    
    "/categories/:id/todos/:id"

    def test_method_restrictions_for_category_todo_endpoint(self):
        category_id = self.test_create_categories()
        todo_id = self.test_create_todo()
        for method in [requests.get, requests.put, requests.post, requests.patch, requests.head]:
            response = method(f"{BASE_URL}/categories/{category_id}/todos/{todo_id}")
            assert response.status_code == 405, f"{method.__name__.upper()} should not be allowed."

    def test_options_for_category_todo_endpoint(self):
        category_id = self.test_create_categories()
        todo_id = self.test_create_todo()
        response = requests.options(f"{BASE_URL}/categories/{category_id}/todos/{todo_id}")
        assert response.status_code == 200

    def test_delete_category_todo_relationship(self):
        """Test deleting the relationship between a category and a todo."""
        category_id = self.test_create_categories()
        todo_id = self.test_create_todo()

        response = requests.delete(f"{BASE_URL}/categories/{category_id}/todos/{todo_id}")
        assert response.status_code in [200, 400, 404]
