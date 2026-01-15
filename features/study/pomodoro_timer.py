import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
             print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
             print()

def pomodoro():
             print("Focus time started (25 minutes)")
    countdown(25)

             print("Break time started (5 minutes)")
    countdown(5)

             print("Pomodoro session completed!")

pomodoro()
