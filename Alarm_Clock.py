from datetime import datetime

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS :- ")
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm.......")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_min == current_min):
                if(alarm_sec == current_sec):
                    print("WAKE UP!!!!!")
                    break