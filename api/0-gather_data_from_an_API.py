#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_list(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.text)
        return

    data = response.json()
    employee_name = data[0]['userId']  # Assuming 'userId' contains the employee's name
    
    completed_tasks = []
    for task in data:
        if task['completed']:
            completed_tasks.append(task['title'])
    
    total_tasks = len(data)

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task_title in completed_tasks:
        print(f"    {task_title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)
