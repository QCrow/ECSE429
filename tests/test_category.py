import requests

BASE_URL = "http://localhost:4567"

class TestClass:

    def test_create_categories(self):
        categories_data = {
            "id": "3",
            "title": "categories_test",
            "description": "test of category 1",
        }

        create_response = requests.post(f"{BASE_URL}/categories", json=categories_data)
        assert create_response.status_code == 201
        categories_id = create_response.json().get("id")
        return categories_id
    
    def test_get_all_categories(self):
        """Test retrieving all categories"""
        get_response = requests.get(f"{BASE_URL}/categories")
        assert get_response.status_code == 200
        categories = get_response.json()
        assert isinstance(categories, dict), "Response should be a dictionary"

    

    def test_update_specific_category(self):
        """Test updating a specific category by ID"""
        category_id = self.test_create_category()
        updated_category_data = {
            "title": "Updated Category Title",
            "description": "Updated category description"
        }
        update_response = requests.put(f"{BASE_URL}/categories/{category_id}", json=updated_category_data)
        assert update_response.status_code == 200, "Expected 200 OK for category update"
        
    
    def test_create_category():
        # Endpoint for creating a new category
        url = f"{BASE_URL}/categories"
        
        # Make a POST request to create a new category
        response = requests.post(url, json=CATEGORY_DATA)
        
        # Verify that the response status code is 200 OK
        assert response.status_code == 200, "Status code is not 200 OK"
        
        # Verify the response contains the required fields
        response_data = response.json()
        assert 'id' in response_data, "Response does not contain 'id'"
        assert response_data['title'] == CATEGORY_DATA['title'], "Title does not match"
        assert response_data['description'] == CATEGORY_DATA['description'], "Description does not match"
        
        