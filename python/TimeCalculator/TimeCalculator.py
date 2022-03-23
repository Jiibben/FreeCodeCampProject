from datetime import timedelta, datetime


daysOfTheWeek = {
    0:"monday",
    1:"tuesday",
    2:"wednesday",
    3:"thursday",
    4:"friday",
    5:"saturday",
    6:"sunday"
}

invertedDaysOfTheWeek = {v:k for (k,v) in daysOfTheWeek.items()}


def add_time(time,increase, day=""):
    givenTime = datetime.strptime(time,'%I:%M %p')
    hours, minute = increase.split(":")
    finalTime = givenTime + timedelta(hours=int(hours), minutes=int(minute))

    dayDifference = finalTime.day - givenTime.day;
    stringTime = datetime.strftime(finalTime,'%I:%M %p') 
    if stringTime.startswith("0") and not stringTime.startswith("00"):
        stringTime = stringTime[1:]
    if day:
       stringTime += ", "+ daysOfTheWeek[(invertedDaysOfTheWeek[day.lower()] + dayDifference) % 7].capitalize()
    
    if dayDifference == 1:
        stringTime += " (next day)"
    elif dayDifference <= 0:
        pass
    else:
        stringTime += f" ({dayDifference} days later)"

    return stringTime




print(add_time("11:30 AM", "100:00", "Monday"))