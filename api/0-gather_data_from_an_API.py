import requests
import sys

def get_employee_info(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Make API requests to get employee info and TODO list
    user_response = requests.get(user_endpoint)
    todos_response = requests.get(todos_endpoint)

    # Check if the requests were successful
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return None, None

    # Parse JSON responses
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract relevant information
    employee_name = user_data.get("name", "Unknown")
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    completed_task_titles = [todo["title"] for todo in todos_data if todo["completed"]]

    return employee_name, total_tasks, completed_tasks, completed_task_titles

def display_todo_progress(employee_name, total_tasks, completed_tasks, completed_task_titles):
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task_title in completed_task_titles:
        print(f"\t{task_title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, total_tasks, completed_tasks, completed_task_titles = get_employee_info(employee_id)

    if employee_name is not None:
        display_todo_progress(employee_name, total_tasks, completed_tasks, completed_task_titles)
