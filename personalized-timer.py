import time
import winsound


def beepAlert(reps, freq, dur):
    for _ in range(reps):
        winsound.Beep(freq, dur)


time.sleep(0.5)
beepAlert(1, 900, 1000)  # Execution alert

try:
    timeSet = int(input("Enter the time in seconds: "))
except ValueError:
    timeSet = int(input("Invalid input. Please enter an integer: "))

for x in range(timeSet, 0, -1):
    secs = x % 60
    mins = int(x // 60) % 60
    hours = int(x // 3600)
    print(f"{hours:02}:{mins:02}:{secs:02}", end="\r")
    time.sleep(1)

print("Time's up!")

beepAlert(4, 1100, 500)  # Final alert sound
