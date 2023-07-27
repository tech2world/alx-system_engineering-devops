#!/usr/bin/python3
"""a script that gathers data from an API"""
import requests
from sys import argv


if __name__ == "__main__":

        employee_id = argv[1]
        api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

        # sending get request to API
        response = requests.get(api_url)

        if response.status_code == 200:
            todo_data = response.json()

            # extract employee information
            employee_name = todo_data[0]["name"] if len(todo_data) > 0 else "Unknown Employee"
            completed_tasks = [task for task in todo_data if task.get('completed')]

            print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")

            for task in completed_tasks:
                print("\t {}".format(task.get('title')))
        else:
            print(f"Error: API request failed with status code {response.status_code}")
