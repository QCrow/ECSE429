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
    
    "end pint with category"
    def test_post_an_empty_category(self):
        create_response = requests.post(f"{BASE_URL}/categories")
        assert create_response.status_code == 400, "bad request"


    def test_get_all_categories(self):
        """Test retrieving all categories"""
        get_response = requests.get(f"{BASE_URL}/categories")
        assert get_response.status_code == 200
        categories = get_response.json()
        assert isinstance(categories, dict), "Response should be a dictionary"

    def test_method_not_allowed_on_base_endpoint(self):
        """Test methods not allowed on the base /categories endpoint"""
        #  PUT on categories endpoint is not allowed
        put_response = requests.put(f"{BASE_URL}/categories", json={})
        assert put_response.status_code == 405, "PUT should not be allowed on base /categories"

        # DELETE  on base categories endpoint is not allowed
        delete_response = requests.delete(f"{BASE_URL}/categories")
        assert delete_response.status_code == 405, "DELETE should not be allowed on base /categories"


        patch_response = requests.patch(f"{BASE_URL}/categories")
        assert patch_response.status_code == 405


    def test_options_on_categories(self):
        """Test the OPTIONS method on the /categories endpoint"""
        options_response = requests.options(f"{BASE_URL}/categories")
        assert options_response.status_code == 200

    def test_head_on_categories(self):
        """Test the HEAD method on the /categories endpoint"""
        head_response = requests.head(f"{BASE_URL}/categories")
        assert head_response.status_code == 200

    def test_patch_method_not_allowed(self):
        """Test PATCH method not allowed on the /categories endpoint"""
        patch_response = requests.patch(f"{BASE_URL}/categories")
        assert patch_response.status_code == 405


    "end pint with category_id"
 
    def test_get_specific_category(self):
        category_id = self.test_create_categories()
        response = requests.get(f"{BASE_URL}/{category_id}")
        assert response.status_code == 200

    def test_update_or_put_specific_category(self):
        """Test updating a specific category by ID"""
        category_id = self.test_create_category()
        updated_category_data = {
            "title": "Updated Category Title",
            "description": "Updated category description"
        }
        update_response = requests.put(f"{BASE_URL}/categories/{category_id}", json=updated_category_data)
        assert update_response.status_code == 200, "Expected 200 OK for category update"

    def test_delete_specific_category(self):
        """Test deleting a specific category by ID"""
        category_id = self.test_create_category()
        delete_response = requests.delete(f"{BASE_URL}/categories/{category_id}")
        assert delete_response.status_code == 200, "Expected 200 OK for category deletion"

    def test_post_specific_category_not_allowed(self):
        category_id = self.test_create_categories()
        data = {"title": "Attempt to Post", "description": "Post Description"}
        response = requests.post(f"{BASE_URL}/{category_id}", json=data)
        assert response.status_code == 405
