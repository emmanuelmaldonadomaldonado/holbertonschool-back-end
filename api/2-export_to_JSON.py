#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her list progress"""
import json
import requests
import sys

def fetch_employee_todo_list(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.text)
        return None
    
    data = response.json()
    employee_name = data[0]['userId']  # Assuming 'userId' contains the employee's name
    
    completed_tasks = []
    for task in data:
        if task['completed']:
            completed_tasks.append(task)

    return {'employee_name': employee_name, 'tasks': completed_tasks}

def export_to_json(employee_id, data):
    if not data:
        return
    
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = fetch_employee_todo_list(employee_id)
    if todo_list:
        export_to_json(employee_id, todo_list)
        print(f"Data exported to {employee_id}.json")
