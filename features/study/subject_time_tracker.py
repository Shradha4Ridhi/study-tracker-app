from datetime import date

study_log = []

def add_study_time():
    subject = input("Enter subject name: ")
    minutes = int(input("Enter time studied (in minutes): "))
    today = date.today()

    study_log.append({
        "subject": subject,
        "minutes": minutes,
        "date": today
    })

          print("Study time logged successfully.\n")

def view_logs():
    if not study_log:
         print("No study records found.\n")
        return

        print("\nStudy Records:")
    for log in study_log:
        print(f"{log['date']} - {log['subject']} : {log['minutes']} minutes")
        print()

while True:
        print("1. Add Study Time")
        print("2. View Study Log")
        print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
       add_study_time()
    elif choice == "2":
       view_logs()
    elif choice == "3":
       print("Exiting program.")
        break
    else:
       print("Invalid choice. Try again.\n")
