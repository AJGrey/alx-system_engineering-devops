#!/usr/bin/python3
"""fetching json data from an api and exporting as JSON"""

import json
import requests

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_dict = requests.get(user_url).json()
    user_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todo = user_todo.json()
    users_tasks = {}

    for user in user_dict:
        user_id = str(user.get("id"))
        user_name = user.get("username")
        user_tasks = []
        for item in user_todo:
            if item.get("userId") == int(user_id):
                task_dict = {}
                task_dict["username"] = user_name
                task_dict["task"] = item.get("title")
                task_dict["completed"] = item.get("completed")
                user_tasks.append(task_dict)
        users_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(users_tasks, json_file, indent=4)
