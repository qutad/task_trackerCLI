import json
import os

db_file = "tasks.json"

def load_tasks():
    if not os.path.exists(db_file):
        return[]
    with open(db_file, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    print(f"\nHint: All tasks will be saved as a tasks.json in the current directory: {os.getcwd()}")
    with open(db_file, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(descripton):
    tasks = load_tasks()
    new_tasks = {
        "id": len(tasks) + 1,
        "description": descripton,
        "status": "todo"
    }
    tasks.append(new_tasks)
    save_tasks(tasks)
    print(f"Task added:{descripton}")

def update_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print(f"Task {task_id} updated to {new_status}")
            return
    print("Tasks not found")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    print(f"\n-- {'All' if not status_filter else status_filter.capitalize()} Tasks ---")
    for task in tasks:
        if status_filter is None or task["status"] == status_filter:
            print(f"[{task['id']}] {task['description']} - {task['status']}")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id ]

    if len(tasks) == len(updated_tasks):
        print(f"Tasks {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"task {task_id} deleted successfully. ")

def main():
    while True:
        print("\n --- Menu ---")
        print("1. Add Task\n"
            "2. List All Tasks\n"
            "3. List by status (done, todo, in-progress)\n"
            "4. Update Task status\n"
            "5. Delete Task\n"
            "to quit -- 'q', or 'quit'")

        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            stat = input('Enter status to filter by (done/todo/in-progress): ')
            list_tasks(stat)
        elif choice == '4':
            try:
                task_id = int(input('Enter task ID: '))
                new_stat = input('Enter new status: ')
                update_status(task_id, new_stat)
            except ValueError:
                print("\n!!!ValueError: Please enter a valid number!!!\n: ")
        elif choice == '5':
            task_id = int(input('Enter task ID to delete: '))
            delete_task(task_id)
        elif choice.lower() in ['q', 'quit']:
            print('Quiting...')
            break
        else:
            print("Invalid choice, please try again. ")

if __name__ == "__main__":
    main()