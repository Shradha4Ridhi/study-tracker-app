# Daily Task Checklist Feature

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks for today.\n")
        return
    print("\nToday's Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['task']} [{status}]")
    print()

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def daily_task_checklist():
    tasks = []
    while True:
        print("Daily Task Checklist")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Exiting Daily Task Checklist.")
            break
        else:
            print("Invalid choice. Try again.\n")

daily_task_checklist()
