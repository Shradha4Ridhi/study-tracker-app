from datetime import date, timedelta

study_days = []
current_streak = 0
longest_streak = 0

def log_study():
    global current_streak, longest_streak

    today = date.today()

    if study_days and today == study_days[-1]:
           print("Today's study already logged.\n")
        return

    study_days.append(today)

    if len(study_days) > 1 and study_days[-1] - study_days[-2] == timedelta(days=1):
        current_streak += 1
    else:
        current_streak = 1

    longest_streak = max(longest_streak, current_streak)

         print("Study day logged successfully.\n")

def view_streak():
         print(f"Current Streak: {current_streak} days")
         print(f"Longest Streak: {longest_streak} days\n")

while True:
       print("1. Log Today's Study")
       print("2. View Streak")
       print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        log_study()
    elif choice == "2":
        view_streak()
    elif choice == "3":
        break
    else:
       print("Invalid choice.\n")
