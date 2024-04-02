import time
import random
import requests

BASE_URL = "http://localhost:4567"

class TestPerformance:

    @staticmethod
    def generate_todo_data():
        todo_data = {
            "title": "Test Todo",
            "doneStatus": random.choice([True, False]),
            "description": "Simple test todo",
        }
        return todo_data

    @staticmethod
    def create_todo():
        todo_data = TestPerformance.generate_todo_data()
        create_response = requests.post(f"{BASE_URL}/todos", json=todo_data)

    @staticmethod
    def delete_todo(todo_id):
        delete_response = requests.delete(f"{BASE_URL}/todos/{todo_id}")

    @staticmethod
    def update_todo(todo_id):
        todo_data = TestPerformance.generate_todo_data()
        update_response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=todo_data)

    @staticmethod
    def measure_time(func, *args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        return end_time - start_time

    @staticmethod
    def test_performance(num_objects):
        create_times = []
        delete_times = []
        update_times = []

        for _ in range(num_objects):
            todo_id = TestPerformance.create_todo()
            create_times.append(TestPerformance.measure_time(TestPerformance.create_todo))
            update_times.append(TestPerformance.measure_time(TestPerformance.update_todo, todo_id))
            delete_times.append(TestPerformance.measure_time(TestPerformance.delete_todo, todo_id))

        return create_times, update_times, delete_times

if __name__ == "__main__":
    num_objects_list = [10, 50, 100, 150, 200, 1000, 1500, 2000]

    for num_objects in num_objects_list:
        print(f"Testing performance for {num_objects} objects:")
        create_times, update_times, delete_times = TestPerformance.test_performance(num_objects)
        
        # print(f"Create Times: {create_times}")
        # print(f"Update Times: {update_times}")
        # print(f"Delete Times: {delete_times}")
        # print("\n")

        create_average = sum(create_times) / len(create_times)
        update_average = sum(update_times) / len(update_times)
        delete_average = sum(delete_times) / len(delete_times)

        print(f"Average Create Time: {create_average}")
        print(f"Average Update Time: {update_average}")
        print(f"Average Delete Time: {delete_average}")
        print("\n")
