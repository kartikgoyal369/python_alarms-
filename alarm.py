from datetime import datetime
import time
import winsound
while True:
    try:
        num_alarms = int(input("how many alarms do you want to set? "))
    except ValueError:
        print("only number allowed1")
        continue
    
    alarm = []
    for i in range(num_alarms):
        while True:
            try:
                time_hour = int(input("set timer in hours: "))
                time_minute = int(input("set timer in minutes: "))
                
            except ValueError:
                print("only number allowed2!!")
                continue
            if time_hour < 0 or time_hour > 23 or time_minute < 0 or time_minute > 59:
                print("invalid time")
                continue
            beep_time =input("do you wank multiple beep?:(y/n) ")
            if beep_time == "n":
                beep_count = 1
                alarm.append((time_hour, time_minute, beep_count))
                break
                
            elif beep_time == "y":
                try:
                    beep_count = int(input("how many beep you want: "))
                    alarm.append((time_hour, time_minute,beep_count))
                except ValueError:
                   print("only number allowed2!!")
                   continue
                break
                    
            if beep_time != "y" and beep_time != "n":
                print("fuck offff!!!!")
                continue
            
            
    while True:
        current_time = datetime.now()
        for time_hour,time_minute,beep_count in alarm[:]:
            if current_time.hour == time_hour and current_time.minute  == time_minute :
                for i in range(beep_count):
                    winsound.Beep(500,3000)
                alarm.remove((time_hour,time_minute,beep_count))
                if len(alarm) == 0:
                    print("all alarm completed")
                    break
                print("get up!!!!!!!!!!")
        time.sleep(15)
        

    
        
        
        
        