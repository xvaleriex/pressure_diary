from Structure import *
def Main_menu():
    """
    :return:
    >>> Main_menu()
    """
    print ("                 1. Show all records")
    print ("                 2. Create new records")
    print ("                 3. Delete records")
    print ("                 4. Change records")
    print ("                 5. Find records")
    print ("                 6. Exit")
    print ("                 7. Save into file ")
    print ("                 8. Load from file ")


def Date_menu():
    """
    :return:
    >>> Date_menu()
    """
    print ("                 1. Diastolic pressure")
    print ("                 2. Systolic pressure")
    print ("                 3. Pulse")
    print ("                 4. Exit")

def File_menu():
    """
    :return:
    >>> File_menu()
    """
    print ("                 1.Pickle file")
    print ("                 2.Yaml file")
    print ("                 3.Json file")

def user_input():
    """
    :return:
    >>> user_input()
    """
    return input()

def show_tip(s):
    """
    :return:
    >>> show_tip()
    """
    print(s)

def displayDayInfo(inf):
    """
    :return:
    >>> displayDayInfo()
    """
    print("Day date is ", inf.day)
    print("Month is ", inf.month)
    print("Year date is ", inf.year)
    print("Part of day - ", inf.times_of_day)
    print("Diastolic_pressure - ", inf.diastolic_pressure)
    print("Systolic_pressure - ", inf.systolic_pressure)
    print("Pulse - ", inf.pulse)


