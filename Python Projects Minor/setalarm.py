import datetime
import time
import winsound
print(datetime.datetime.now())
def set_alarm():
    print("Set Your Alarm Please")
    alarm_str=input("Set the alarm in format (HH:MM:SS):")
    try:
        alarm_hour,alarm_min,alarm_sec= map(int,alarm_str.split(":"))
    except ValueError:
        print(f"Please enter the alarm in right format")
        return
    print("Alarm set successfully! Waiting to awake you..")

    while True:
        current_time=datetime.datetime.now()
        if(current_time.hour==alarm_hour,
           current_time.minute==alarm_min,
           current_time.second==alarm_sec):
            print("Ok, its time to wakeup!")
            try:
                winsound.PlaySound("myalarmbeep.wav",winsound.SND_FILENAME)
            except Exception as e:
                print("Could not play sound! Reason: {e}")
            break
        time.sleep(1)
            
set_alarm()