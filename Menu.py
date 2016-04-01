from Structure import *
def Main_menu():
    print ("                 1. Show all records")
    print ("                 2. Create new records")
    print ("                 3. Delete records")
    print ("                 4. Change records")
    print ("                 5. Find records")
    print ("                 6. Exit")

def Date_menu():

    print ("                 1. Diastolic pressure")
    print ("                 2. Systolic pressure")
    print ("                 3. Pulse")
    print ("                 4. Exit")

def user_input():
    return input()

def show_tip(s):
    print(s)

def displayDayInfo(inf):
        print("Day date is ", inf.day)
        print("Month is ", inf.month)
        print("Year date is ", inf.year)
        print("Part of day - ", inf.times_of_day)
        print("Diastolic_pressure - ", inf.diastolic_pressure)
        print("Systolic_pressure - ", inf.systolic_pressure)
        print("Pulse - ", inf.pulse)


