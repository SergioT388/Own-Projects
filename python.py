import time
import winsound


def beepAlert(reps, freq, dur):
    for _ in range(reps):
        winsound.Beep(freq, dur)


def congratsUser(name):
    print(f"Well done, {name}!")


name = str(input("Enter your name, dear user: "))
time.sleep(0.5)  # Espera breve antes de iniciar el conteo
beepAlert(1, 1250, 1000)  # Aviso de ejecución

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
    beepAlert(1, 1000, 300)  # Alert sound every second

print("Time's up!")

beepAlert(4, 1100, 500)  # Final alert sound

congratsUser(name)
