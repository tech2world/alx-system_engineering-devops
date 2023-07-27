#!/usr/bin/python3
"""exporting data to a json file"""
from sys import argv
import json
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

    json_dict = {employee_id: []}

    for task in tasks:
        json_dict[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })

    file_name = employee_id + '.json'

    with open(file_name, 'w') as file:
        json.dump(json_dict, file)
