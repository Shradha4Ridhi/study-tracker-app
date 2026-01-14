# Daily Study Log Feature
# This module allows users to log daily study activity

study_log = []

def add_study_entry(date, subject, minutes, notes=""):
    entry = {
        "date": date,
        "subject": subject,
        "minutes": minutes,
        "notes": notes
    }
    study_log.append(entry)
            print("Study entry added successfully.")

def view_study_log():
    if not study_log:
            print("No study entries found.")
        return

    for entry in study_log:
           print("----------------------")
           print("Date:", entry["date"])
           print("Subject:", entry["subject"])
           print("Time Studied:", entry["minutes"], "minutes")
        if entry["notes"]:
           print("Notes:", entry["notes"])

# Example 
add_study_entry("2026-01-11", "Python", 60, "Worked on daily study log feature")
add_study_entry("2026-01-11", "Math", 45)

view_study_log()
