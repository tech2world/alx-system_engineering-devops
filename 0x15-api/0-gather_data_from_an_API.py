#!/usr/bin/python3
"""a script that gathers data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    # get employee id from command line
    employee_id = argv[1]
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # sending get request to API
    response = requests.get(api_url)
    todo_task = response.json()

    # extract employee information
    name = response.json().get('name')
    task = 0
    todo_task = []

    for todo in todo_task:
        if todo.get('completed'):
            todo_task.append(todo)
            task += 1
    
    print("Employee {} is done with tasks({}/{}):"
          .format(name, task, len(todo_task)))
    
    for task in todo_task:
        print("\t {}".format(task.get('title')))
