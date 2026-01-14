# Weekly Study Planner Feature
# This module helps plan study tasks for the week

weekly_plan = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

def add_task(day, subject, duration):
    if day in weekly_plan:
        task = {
            "subject": subject,
            "duration": duration
        }
        weekly_plan[day].append(task)
            print("Task added to", day)
    else:
            print("Invalid day entered.")

def view_weekly_plan():
    for day, tasks in weekly_plan.items():
            print("\n" + day)
        if not tasks:
            print("  No tasks planned.")
        else:
            for task in tasks:
            print("  Subject:", task["subject"], "-", task["duration"], "minutes")

# Example usage
add_task("Monday", "Physics", 60)
add_task("Monday", "Python", 45)
add_task("Wednesday", "Chemistry", 50)

view_weekly_plan()
