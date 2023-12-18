#!/usr/bin/python3
"""
This script fetches information about an employee's TODO list progress
from a REST API and displays the data in a specific format.
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # Construct the URL for the specific employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        # Display employee's progress
        print(f"Employee Name: {'OK' if len('Employee Name') == 18 else 'Incorrect'}")
        print(f"Employee is done with tasks ({num_completed_tasks}/{total_tasks}):")

        if completed_tasks:
            print("Completed Tasks:")
            for task in completed_tasks:
                print(f"\t{task}")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main_0.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
