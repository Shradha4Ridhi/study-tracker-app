# Priority-Based Tasks Feature

def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Set priority (High / Medium / Low): ").capitalize()
    tasks.append({"task": task, "priority": priority})
    print("Task added successfully.\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 4))

    print("\nPriority-Based Task List:")
    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task['task']} [Priority: {task['priority']}]")
    print()

def priority_task_manager():
    tasks = []
    while True:
            print("Priority-Based Task Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Exiting Priority Task Manager.")
            break
        else:
            print("Invalid choice. Try again.\n")

priority_task_manager()
