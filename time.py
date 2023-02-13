currentTime = int(input("Enter the current time: "))
hoursRequired = int(input("After how many hours do you want the alarm to sound: "))
updatedHours = hoursRequired
timeElapsed = 0
days = 0

timeRemaining = hoursRequired%24
alarmTime = timeRemaining + currentTime
if alarmTime > 24:
    alarmTime -= 24
    print("Alarm Time", alarmTime)
else:
    print("Alarm Time", alarmTime)