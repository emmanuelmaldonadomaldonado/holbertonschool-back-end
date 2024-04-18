#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her list progress"""
import json
import requests

def fetch_all_employees_todo_list():
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.text)
        return None

    data = response.json()
    all_employees_tasks = {}

    for task in data:
        user_id = str(task['userId'])
        task_info = {
            'username': task['userId'],
            'task': task['title'],
            'completed': task['completed']
        }
        if user_id in all_employees_tasks:
            all_employees_tasks[user_id].append(task_info)
        else:
            all_employees_tasks[user_id] = [task_info]

    return all_employees_tasks

def export_to_json(data):
    if not data:
        return
    
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    all_employees_tasks = fetch_all_employees_todo_list()
    if all_employees_tasks:
        export_to_json(all_employees_tasks)
        print("Data exported to todo_all_employees.json")
