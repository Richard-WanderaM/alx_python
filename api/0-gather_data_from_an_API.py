import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    # Fetch employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employee TODO list
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_data = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)
    completed_task_count = len(completed_tasks)

    # Display TODO list progress
print(f"Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t{task['title']}")

