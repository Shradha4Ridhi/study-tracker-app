# Long-Term Academic Goals Feature

def add_goal(goals):
    goal = input("Enter your academic goal: ")
    timeline = input("Enter target timeline (e.g., 6 months, 1 year): ")
    goals.append({"goal": goal, "timeline": timeline})
    print("Goal added successfully.\n")

def view_goals(goals):
    if not goals:
        print("No academic goals set yet.\n")
        return
    print("\nLong-Term Academic Goals:")
    for i, goal in enumerate(goals, start=1):
        print(f"{i}. {goal['goal']} (Target: {goal['timeline']})")
    print()

def academic_goals_tracker():
    goals = []
    while True:
        print("Academic Goals Tracker")
        print("1. Add Goal")
        print("2. View Goals")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_goal(goals)
        elif choice == "2":
            view_goals(goals)
        elif choice == "3":
            print("Exiting Academic Goals Tracker.")
            break
        else:
            print("Invalid choice. Try again.\n")

academic_goals_tracker()
