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