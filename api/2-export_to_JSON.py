import requests
import sys
import json

def get_employee_info(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    user_response = requests.get(user_endpoint)
    todos_response = requests.get(todos_endpoint)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return None, None, None, None

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name", "Unknown")
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    completed_task_titles = [todo["title"] for todo in todos_data if todo["completed"]]

    return employee_name, total_tasks, completed_tasks, completed_task_titles

def display_todo_progress(employee_name, total_tasks, completed_tasks, completed_task_titles):
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task_title in completed_task_titles:
        print(f"\t{task_title}")

def export_to_json(employee_id, completed_task_data):
    data = {str(employee_id): [{"task": task, "completed": True, "username": employee_name} for task in completed_task_data]}
    filename = f"{employee_id}.json"

    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, total_tasks, completed_tasks, completed_task_titles = get_employee_info(employee_id)

    if employee_name is not None:
        display_todo_progress(employee_name, total_tasks, completed_tasks, completed_task_titles)

        # Export data to JSON
        export_to_json(employee_id, completed_task_titles)
