#!/usr/bin/python3
"""fetching json data from an api and exporting as JSON"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    user_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todo = user_todo.json()
    tasks = []

    for item in user_todo:
        if item.get("userId") == int(user_id):
            task_dict = {}
            task_dict["task"] = item.get("title")
            task_dict["completed"] = item.get("completed")
            task_dict["username"] = user_name
            tasks.append(task_dict)
    
    json_data = {user_id: tasks}
    with open("USER_ID.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
