#!/usr/bin/python3
""" a script to get data using API"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Error: Please provide an employee ID as a command-line argument.")
    else:
        employee_id = argv[1]
        api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

        # Sending a get request to API for employee info
        response = requests.get(api_url)

        if response.status_code == 200:
            employee_data = response.json()
            employee_name = employee_data.get('name', 'Unknown Employee')

            # Sending a get request to API for employee's TODO tasks
            todo_url = api_url + '/todos'
            response = requests.get(todo_url)

            if response.status_code == 200:
                todo_data = response.json()
                completed_tasks = [task for task in todo_data if task.get('completed')]

                print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")

                for task in completed_tasks:
                    print("\t{}".format(task.get('title')))
            else:
                print(f"Error: API request for TODO tasks failed with status code {response.status_code}")
                exit(1)
        else:
            print(f"Error: API request for employee info failed with status code {response.status_code}")
            exit(1)
