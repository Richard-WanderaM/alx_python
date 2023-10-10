"""
This script retrieves employee TODO list progress and exports it to a JSON file.

Usage: python3 2-export_to_JSON.py <employee_id>

Arguments:
    employee_id (int): The employee ID to retrieve TODO list progress for.

Example:
    python3 2-export_to_JSON.py 2
"""

import requests
import json
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    # Fetch employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employee TODO list
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_data = todos_response.json()

    # Filter tasks owned by this employee
    employee_tasks = [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todos_data]

    # Create a dictionary for JSON export
    export_data = {employee_id: employee_tasks}

    # Export to JSON file
    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(export_data, json_file)

    print(f"Data exported to {employee_id}.json")

