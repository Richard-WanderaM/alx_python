import json
import requests
import sys

def get_employee_todo_list(employee_id):
    """
    Fetches the todo list for a given employee from a mock API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing employee name and todo list data.
    """
    # Fetch employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get('name', 'Unknown')

    # Fetch todo list for the employee
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    return employee_name, todo_data

def export_to_json(filename, data):
    """
    Exports data to a JSON file.

    Args:
        filename (str): The name of the output JSON file.
        data (dict): The data to be exported.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, todo_list = get_employee_todo_list(employee_id)

    todo_dict = {}
    for task in todo_list:
        user_id = str(employee_id)
        task_data = {
            "username": employee_name,
            "task": task["title"],
            "completed": task["completed"]
        }

        if user_id not in todo_dict:
            todo_dict[user_id] = []

        todo_dict[user_id].append(task_data)

    # Export to JSON
    filename = "todo_all_employees.json"
    export_to_json(filename, todo_dict)
    print(f"Data exported to {filename}")
