
from datetime import datetime
from playsound import playsound

def main():

    alarm_time = input("Enter the alarm time:HH:MM:SS\n ")
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_second = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    print("Setting up alarm...")
    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_second = now.strftime("%S")
        current_period = now.strftime("%p")
        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_minute == current_minute:
                    if alarm_second == current_second:
                        print("Wake up!")
                        playsound('audio.mp3')
                        break


main()


