import time
import random
import requests
import psutil
import os
import matplotlib.pyplot as plt

BASE_URL = "http://localhost:4567"


class TestPerformance:

    @staticmethod
    def generate_project_data():
        project_data = {"title": "Test Project"}
        return project_data

    @staticmethod
    def create_project():
        project_data = TestPerformance.generate_project_data()
        create_response = requests.post(f"{BASE_URL}/projects", json=project_data)

    @staticmethod
    def delete_project(project_id):
        delete_response = requests.delete(f"{BASE_URL}/projects/{project_id}")

    @staticmethod
    def update_project(project_id):
        project_data = {"title": "Updated Project"}
        update_response = requests.put(
            f"{BASE_URL}/projects/{project_id}", json=project_data
        )

    @staticmethod
    def measure_time(func, *args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        return end_time - start_time

    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent()

    @staticmethod
    def get_free_memory():
        return psutil.virtual_memory().available / (1024**2)  # Convert to MB

    @staticmethod
    def get_system_stats():
        return TestPerformance.get_cpu_usage(), TestPerformance.get_free_memory()

    @staticmethod
    def test_performance(num_objects):
        create_times = []
        delete_times = []
        update_times = []
        cpu_percents = []
        free_memorys = []

        for _ in range(num_objects):
            project_id = TestPerformance.create_project()
            create_times.append(
                TestPerformance.measure_time(TestPerformance.create_project)
            )
            update_times.append(
                TestPerformance.measure_time(TestPerformance.update_project, project_id)
            )
            delete_times.append(
                TestPerformance.measure_time(TestPerformance.delete_project, project_id)
            )
            cpu_percent, free_memory = TestPerformance.get_system_stats()
            cpu_percents.append(cpu_percent)
            free_memorys.append(free_memory)

        return create_times, update_times, delete_times, cpu_percents, free_memorys


if __name__ == "__main__":
    num_objects_list = [10, 50, 100, 150, 200, 300, 500, 1000]

    create_averages = []
    update_averages = []
    delete_averages = []
    cpu_averages = []
    free_memory_averages = []

    for num_objects in num_objects_list:
        print(f"Testing performance for {num_objects} objects:")
        create_times, update_times, delete_times, cpu_percents, free_memorys = (
            TestPerformance.test_performance(num_objects)
        )
        create_average = sum(create_times) / len(create_times)
        update_average = sum(update_times) / len(update_times)
        delete_average = sum(delete_times) / len(delete_times)
        cpu_average = sum(cpu_percents) / len(cpu_percents)
        free_memory_average = sum(free_memorys) / len(free_memorys)

        # Print results to terminal
        print(f"Average Create Time: {create_average}")
        print(f"Average Update Time: {update_average}")
        print(f"Average Delete Time: {delete_average}")
        print(f"Average CPU Usage: {cpu_average}")
        print(f"Average Free Memory: {free_memory_average}")
        print("\n")

        # Prepare data for plotting
        cpu_averages.append(cpu_average)
        free_memory_averages.append(free_memory_average)
        create_averages.append(create_average)
        update_averages.append(update_average)
        delete_averages.append(delete_average)

    # Plotting
    plt.figure(figsize=(10, 10))

    # Time
    plt.subplot(3, 1, 1)
    plt.plot(num_objects_list, create_averages, label="Create Time")
    plt.plot(num_objects_list, update_averages, label="Update Time")
    plt.plot(num_objects_list, delete_averages, label="Delete Time")
    plt.xlabel("Number of Objects")
    plt.ylabel("Average Time")
    plt.title("Average Time vs Number of Objects")
    plt.legend()

    # CPU Usage
    plt.subplot(3, 1, 2)
    plt.plot(num_objects_list, cpu_averages, label="CPU Percent Usage")
    plt.xlabel("Number of Objects")
    plt.ylabel("CPU Percent Usage")
    plt.title("CPU Percent Usage vs Number of Objects")
    plt.legend()

    # Free Memory
    plt.subplot(3, 1, 3)
    plt.plot(
        num_objects_list, free_memory_averages, label="Free Memory (MB)", color="green"
    )
    plt.xlabel("Number of Objects")
    plt.ylabel("Free Memory (MB)")
    plt.title("Free Memory vs Number of Objects")
    plt.legend()

    plt.tight_layout()
    plt.show()
