#!/usr/bin/python3
"""exporting data to a csv file"""
from sys import argv
import requests


if __name__ == "__main__":
    employee_id = argv[1]
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # get username from API
    response = requests.get(api_url)
    username = response.json().get('username')

    # get todo list
    todo_url = api_url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    # write the data to a CSV file, using a context manager
    file_name = employee_id + '.csv'

    with open(file_name, "w") as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'), task.get('title')))
