#!/usr/bin/python3
""" a script to get data using API"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Error: Please provide an employee ID.")
    else:
        employee_id = argv[1]
        api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

        # Sending a get request to API for employee info
        response = requests.get(api_url)

        employee_data = response.json()
        employee_name = employee_data.get('name', 'Unknown Employee')

        # Sending a get request to API for employee's TODO tasks
        todo_url = api_url + '/todos'
        response = requests.get(todo_url)

        todo_data = response.json()
        completed_tasks = [task for task in todo_data if task.get('completed')]

        print(f"Employee {employee_name} is done with tasks({
            len(completed_tasks)}/{len(todo_data)}):")

        for task in completed_tasks:
            print("\t{}".format(task.get('title')))
