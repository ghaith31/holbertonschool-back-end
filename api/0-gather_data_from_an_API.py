#!/usr/bin/python3
"""
Retrieves TODO list progress for a given employee ID from a REST API.
"""

import requests
import sys

def fetch_employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    try:
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)
        todos_response.raise_for_status()
        user_response.raise_for_status()
    except requests.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return

    todos_data = todos_response.json()
    user_data = user_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_list(employee_id)
