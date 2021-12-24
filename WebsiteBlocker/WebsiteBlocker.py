from datetime import datetime as dt
import stat
import os

def main():
    timeOfEventStart = getEventStartTime()
    timeOfEventEnd = getEventEndTime()
    ipAddress = getIPAddress().strip()
    websitesToBlock = ""
    websitePath = "websites"
    hostPath = "hosts"
 
    while(True):
        timeNow = dt.now(tz = None).replace(microsecond = 0)
        print("Time until event: ",timeNow, timeOfEventStart, end = '\r')

        if timeOfEventStart <= timeNow:
            print('\n')
            os.system('sudo cp /etc/hosts .')
            os.system('sudo chmod 646 hosts')

            with open(websitePath, "r") as website:
                websitesToBlock = website.readlines()

            with open(hostPath, "r+") as host:
                hostFile = host.read()

                for websites in websitesToBlock:
                    if websites in hostFile:
                        continue
                    else:
                        host.write(ipAddress + " " + websites)

            os.system('sudo chmod 644 hosts')
            os.system('sudo cp hosts /etc/hosts')
            break

    while(True):
        timeNow = dt.now(tz = None).replace(microsecond = 0)
        print("Time until end of event: ", timeNow, timeOfEventEnd, end = '\r')
        
        if timeNow >= timeOfEventEnd:
            print('\n')
            os.system('sudo chmod 646 hosts')

            with open("hosts", "r+") as host:
                hostFile = host.readlines()
                host.seek(0)

                for line in hostFile:
                    if not any(page in line for page in websitesToBlock):
                        host.write(line)

                host.truncate()

            os.system('sudo chmod 644 hosts')
            os.system('sudo cp hosts /etc/hosts')
            break

def getEventStartTime():
    year = int(input("Enter year of the event: "))
    while(year < dt.now(tz = None).year):
        year = int(input("Enter year of the event: "))

    month = int(input("Enter month of the event: "))
    while(month < 1 or month > 12):
        month = int(input("Enter month of the event: "))

    day = int(input("Enter day of the event: "))
    thisMonth = dt.now(tz = None).month
    if (thisMonth == 1 or thisMonth == 3 or thisMonth == 5 or thisMonth == 7 or thisMonth == 8
        or thisMonth == 10 or thisMonth == 12):
            while (day < 1 or day > 31):
                day = int(input("Enter day of the event: "))
    elif (thisMonth == 2):
        while (day < 1 or day > 28):
            day = int(input("Enter day of the event: "))

    elif (thisMonth == 4 or thisMonth == 6 or thisMonth == 9 or thisMonth == 11):
        while (day < 1 or day > 30):
            day = int(input("Enter day of the event: "))

    hour = int(input("Enter hour of the event in military time format 0 - 24: "))
    while (hour < 0 or hour > 24):
        hour = int(input("Enter hour of the event: "))

    minute = int(input("Enter minute of the event 0 - 59: "))
    while (minute < 0 or minute > 59):
         minute = int(input("Enter minute of the event: "))

    timeOfEventStart = dt(year, month, day, hour, minute , 0, 0)
    return timeOfEventStart

def getEventEndTime():
    year = int(input("Enter year for the end of event: "))
    while(year < dt.now(tz = None).year):
        year = int(input("Enter year for the end of event: "))

    month = int(input("Enter month for the end of event: "))
    while(month < 1 or month > 12):
        month = int(input("Enter month for the end of event: "))

    day = int(input("Enter day for the end of event: "))
    thisMonth = dt.now(tz = None).month
    if (thisMonth == 1 or thisMonth == 3 or thisMonth == 5 or thisMonth == 7 or thisMonth == 8
        or thisMonth == 10 or thisMonth == 12):
            while (day < 1 or day > 31):
                day = int(input("Enter day for the end of event: "))
    elif (thisMonth == 2):
        while (day < 1 or day > 28):
            day = int(input("Enter day for the end of event: "))

    elif (thisMonth == 4 or thisMonth == 6 or thisMonth == 9 or thisMonth == 11):
        while (day < 1 or day > 30):
            day = int(input("Enter day for the end of event: "))

    hour = int(input("Enter hour for the end of event in military time format 0 - 24: "))
    while (hour < 0 or hour > 24):
        hour = int(input("Enter hour for the end of event: "))

    minute = int(input("Enter minute for the end of event 0 - 59: "))
    while (minute < 0 or minute > 59):
         minute = int(input("Enter minute for the end of event: "))

    timeOfEventEnd = dt(year, month, day, hour, minute , 0, 0)
    return timeOfEventEnd

def getIPAddress():
    stream = os.popen("hostname -I | awk '{print $1}'")
    output = stream.read()
    return output

main()