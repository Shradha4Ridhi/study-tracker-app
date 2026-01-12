study_log = []

def add_study_session(subject, minutes):
    session = {
        "subject": subject,
        "minutes": minutes
    }
    study_log.append(session)

def view_daily_log():
    if not study_log:
        print("No study sessions recorded today.")
        return

    print("\nDaily Study Log:")
    for i, session in enumerate(study_log, start=1):
        print(f"{i}. {session['subject']} - {session['minutes']} minutes")

def get_total_study_time():
    total_minutes = sum(session["minutes"] for session in study_log)
    return total_minutes


# Example usage
if __name__ == "__main__":
     add_study_session("Mathematics", 60)
     add_study_session("Computer Science", 90)

view_daily_log()
     print(f"\nTotal study time: {get_total_study_time()} minutes")
