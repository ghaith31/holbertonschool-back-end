#!/usr/bin/python3

"""
Fetches information about an employee's TODO list progress.
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        # Display employee's progress
        print(f"Employee Name: {'OK' if len(employee_name) == 18 else 'Incorrect'}")
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        print(f"\tEmployee Name: {employee_name}")
        print(f"\tNumber of Completed Tasks: {num_completed_tasks}")
        print(f"\tTotal Number of Tasks: {total_tasks}")

        if completed_tasks:
            print("\tCompleted Tasks:")
            for task in completed_tasks:
                print(f"\t\t{task}")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main_0.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
