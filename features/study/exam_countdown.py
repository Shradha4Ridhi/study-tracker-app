# Exam Countdown Feature

from datetime import datetime

def exam_countdown():
    exam_name = input("Enter exam name: ")
    exam_date_input = input("Enter exam date (DD-MM-YYYY): ")

    try:
        exam_date = datetime.strptime(exam_date_input, "%d-%m-%Y")
        today = datetime.now()
        days_left = (exam_date - today).days

        if days_left > 0:
            print(f"{days_left} days left for {exam_name}. Stay focused!")
        elif days_left == 0:
            print(f"Today is {exam_name}. All the best!")
        else:
            print(f"{exam_name} has already passed.")
    except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

exam_countdown()
