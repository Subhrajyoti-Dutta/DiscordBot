import datetime
import csv

event_id = datetime.datetime.now().strftime('%m%d%H%M')
event_name = input("Enter the name of the event: ")
reg_start  = input("Enter the starting date of registration(YYYY-MM-DD): ")
reg_end    = input("Enter the ending date of registration(YYYY-MM-DD): ")
event_start= input("Enter the starting date of event(YYYY-MM-DD): ")
event_end  = input("Enter the starting date of event(YYYY-MM-DD): ")
tot_part   = input("Maximum number of participants (write -1 if no limit): ")

print(f"""
Event Id:                   {event_id}
Event Name:                 {event_name}
Registration Start:         {reg_start}
Registration End:           {reg_end}
Starting Date:              {event_start}
Ending Date:                {event_end}
Total participants allowed: {tot_part}
""")

all_ok = input("Do you want to continue(Y/N): ")
if all_ok.upper() != "N":
    with open("events.csv","a") as fl:
        fl.write(f"\n{event_id},{event_name},{reg_start},{reg_end},{event_start},{event_end},{tot_part}")