from datetime import date, timedelta

study_dates = []

def log_study():
    today = date.today()
    if today not in study_dates:
        study_dates.append(today)
         print("Study session logged.\n")
    else:
          print("Already logged for today.\n")

def check_consistency():
    today = date.today()
    last_7_days = [today - timedelta(days=i) for i in range(7)]

    studied_days = sum(1 for d in last_7_days if d in study_dates)
    consistency = (studied_days / 7) * 100

         print(f"Study days in last 7 days: {studied_days}/7")
         print(f"Weekly Consistency: {consistency:.2f}%\n")

while True:
         print("1. Log Study")
         print("2. View Consistency")
         print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        log_study()
    elif choice == "2":
        check_consistency()
    elif choice == "3":
        break
    else:
           print("Invalid option.\n")
