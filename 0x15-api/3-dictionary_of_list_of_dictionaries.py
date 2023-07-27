#!/usr/bin/python3
"""exporting data to a json file"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"

    # get users from API
    response = requests.get(api_url)
    users = response.json()

    # putting the result of the get request in a dict
    dict = {}

    # get todo list
    for user in users:
        user_id = user.get('id')
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)
        tasks = response.json()

        dict[user_id] = []

        for task in tasks:
            dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": task.get('username')
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict, file)
