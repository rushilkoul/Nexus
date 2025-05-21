PERMISSIONLEVEL = 1
import datetime
import json
from utils.permission_checker import check_permission
from utils.log import inf

# TODO: currently program answers "what is n period" from the database. I have to implement "when is x period" queries.
# example: currently it will answer "what is 3rd period" ==== "maths" but it should also answer "when is maths today" ==== "3rd period"

def day_shifter(day, shift):
    day = day + shift
    if day > 6:
        day = day - 7
    return day 
def get_period(_query):
    if check_permission(PERMISSIONLEVEL) == True:
        return _get_period(_query)
    else:
        return check_permission(PERMISSIONLEVEL) 

def _get_period(_query):
    _data = json.load(open("utils/data/data.json"))
    room = _data["localVars"]["installedRoom"]
    day = datetime.datetime.today().weekday()
    if day == 6:
        return "It's Sunday, there are no classes scheduled today."
    
    if "day after tomorrow" in _query:
        day = day_shifter(day, 2)
        if day == 6:
            return "The day after tomorrow is a Sunday, there are no classes scheduled."
    elif "tomorrow" in _query:
        day = day_shifter(day, 1)
        if day == 6:
            return "Tomorrow is a Sunday, there are no classes scheduled."
        
    if "day before yesterday" in _query:
        day = day_shifter(day, -2)
        if day == 6:
            return "The day before yesterday was a Sunday, there were no classes scheduled."
    elif "yesterday" in _query:
        day = day_shifter(day, -1)
        if day == 6:
            return "Yesterday was a Sunday, there were no classes scheduled."
    
    if "on" in _query:
        if "monday" in _query:
            day = 0
        elif "mon" in _query:
            day = 0
        elif "tuesday" in _query:
            day = 1
        elif "tue" in _query:
            day = 1
        elif "wednesday" in _query:
            day = 2
        elif "wed" in _query:
            day = 2
        elif "thursday" in _query:
            day = 3
        elif "thu" in _query:
            day = 3
        elif "friday" in _query:
            day = 4
        elif "fri" in _query:
            day = 4
        elif "saturday" in _query:
            day = 5
        elif "sat" in _query:
            day = 5
        elif "sunday" in _query:
            return "Sunday is a holiday. There are no classes scheduled."
        elif "sun" in _query:
            return "Sunday is a holiday. There are no classes scheduled."


    query = _query.split(" ")
    inf("adminLogs", _query, f"TIME TABLE REQUESTED FOR CLASS {room}")

    number = str(clean_index(query[query.index("period") - 1]))
    if number == 'error_uninmplemented':
        return "That is not implemented yet. Please try again later."
    if number == 'error_out_of_range':
        return "That is not a valid period. Please choose from 1 to 8."
    
    number = int(number)

    #### retrieve actual timetable data    
    timetables = _data["timetables"]
    return timetables[room][day][number]

def clean_index(_index):
    if 'zeroth' in _index:
        return 0
    elif 'zero' in _index:
        return 0
    elif 'first' in _index:
        return 1
    elif 'second' in _index:
        return 2
    elif 'third' in _index:
        return 3
    elif 'fourth' in _index:
        return 4
    elif 'fifth' in _index:
        return 5
    elif 'sixth' in _index:
        return 6
    elif 'seventh' in _index:
        return 7
    elif 'eighth' in _index:
        return 8
    
    elif '0' in _index:
        return 0
    elif '0th' in _index:
        return 0
    elif '1st' in _index:
        return 1
    elif '2nd' in _index:
        return 2
    elif '3rd' in _index:
        return 3
    elif '4th' in _index:
        return 4
    elif '5th' in _index:
        return 5
    elif '6th' in _index:
        return 6
    elif '7th' in _index:
        return 7
    elif '8th' in _index:
        return 8
    
    elif 'last' in _index:
        return 8
    ###### TODO: ADD THIS FEATURE ########
    elif 'next' in _index:
        return 'error_uninmplemented'
    
    else:
        return 'error_out_of_range'