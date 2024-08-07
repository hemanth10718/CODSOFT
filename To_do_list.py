tasks = []

def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def list_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, 1): 
            print(f"Task #{index}. {task}")

def update_task():
    list_tasks()
    try:
        task_to_update = int(input("Enter the # of the task to update: ")) - 1
        if 0 <= task_to_update < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_to_update] = new_task
            print(f"Task #{task_to_update + 1} has been updated to: {new_task}")
        else:
            print(f"Task #{task_to_update + 1} was not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the # of the task to delete: ")) - 1
        if 0 <= task_to_delete < len(tasks):
            removed_task = tasks.pop(task_to_delete)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print(f"Task #{task_to_delete + 1} was not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\nPlease select one of the following options:")
        print("1. Add a new task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
