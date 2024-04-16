import requests
import csv
import sys

def fetch_employee_todo_list(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.text)
        return None
    return response.json()

def export_to_csv(employee_id, data):
    if not data:
        return
    
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': task['userId'],  # Assuming 'userId' contains the username
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = fetch_employee_todo_list(employee_id)
    if todo_list:
        export_to_csv(employee_id, todo_list)
        print(f"Data exported to {employee_id}.csv")
