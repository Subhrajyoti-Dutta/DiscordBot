import datetime

def reply(msg):

    response = ''

    if msg.content.lower() == "hi":
        response += f"""Hello {msg.author}! If you want help, the choose from the following options\n1. Events"""

    elif msg.content.lower() == "1":
        with open("events.csv", "r") as fl:
            num_of_events = 0
            fl = list(fl.readlines())[1:]
            for i in fl:
                info = i.split(',')
                print(info)
                d = datetime.date.fromisoformat(info[4])
                if datetime.datetime.now() < datetime.datetime(d.year,d.month,d.day):
                    num_of_events += 1
                    response += f"\n{info[0]} {info[1]}"

            if num_of_events != 0:
                response = "Here are the upcoming events: " + response + "\nIf you want more info about a specific event, then type \"Event <event id>\""
            else:
                response = "No upcoming events"

    elif msg.content.lower()[:5] == 'event':
        event_id = msg.content[-8:]
        with open("events.csv", "r") as fl:
            events = list(fl.readlines())[1:]
            for i in events:
                if i[:8] == event_id:
                    info = i.split(',')
                    response += f"""
Event Id: {info[0]}
Event Name: {info[1]}
Registration Start: {info[2]}
Registration End: {info[3]}
Starting Date: {info[4]}
Ending Date: {info[5]}
Total participants allowed: {info[6]}
"""
                    break

    else:
        response += "I don't understand"

    return response