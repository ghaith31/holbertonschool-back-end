#!/usr/bin/python3

"""
Retrieve employee TODO list progress using REST API
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(base_url)

    if response.status_code != 200:
        print("Error:", response.json().get('message', 'Failed to retrieve data.'))
        return

    todos = response.json()
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)
    employee_name = todos[0]['username'] if todos else 'Unknown'

    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
