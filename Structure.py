import pickle
from Menu import *

class CalendarDay:
    def __init__(self, day,month,year, times_of_day, diastolic_pressure, systolic_pressure, pulse):
        self.day = day
        self.month = month
        self.year = year
        self.times_of_day = times_of_day
        self.diastolic_pressure = diastolic_pressure
        self.systolic_pressure = systolic_pressure
        self.pulse = pulse

    def getList(self):
        dict = {"day" : self.day, "month": self.month ,"year" : self.year ,
                "times_of_day": self.times_of_day ,
                "diastolic_pressure" :self.diastolic_pressure ,
                "systolic_pressure" : self.systolic_pressure ,"pulse" : self.pulse }
        return dict
    def self_print(self):
        print (self.day,self.month ,self.year, self.times_of_day ,self.diastolic_pressure, self.systolic_pressure ,self.pulse)

    def setNewTimes_of_day(self, times_of_day):
        self.times_of_day = times_of_day

    def setNewDiastolic_pressure(self, diastolic_pressure):
        self.diastolic_pressure = diastolic_pressure

    def setNewSystolic_pressure(self, systolic_pressure):
        self.systolic_pressure = systolic_pressure

    def setNewPulse(self, pulse):
        self.pulse = pulse

diary = []
diaryToSave = []

def run(temp):
    for i in temp :
        diaryToSave.append(i.getList())
    return diaryToSave



def getAllRecords():
    """
    Возвращает все записи
    :return: записи дневника
    >>> getAllRecords()
    [9.9.2009.'morning'.65.45]
    """
    return diary


def CreateRecord(day, month, year, times_of_day, diastolic_pressure, systolic_pressure, pulse):
    """
    Создает новую запись. Условие выполнение функции: отсутствие идентичного обьекта
    >>>
    :param day: день, в котором осуществляется запись
    :param month: месяц, в котором осуществляется запись
    :param year: год, в котором осуществляется запись
    :param times_of_day: время дня, в котором осуществляются замеры
    :param diastolic_pressure: значение верхнего давления
    :param systolic_pressure: значение нижнего давления
    :param pulse: пульс
    :return:
    >>> CreateRecord(9,9,2009,"morning",65,60,45)
    """
    for i in diary:
        if ((i.day == day) and (i.times_of_day == times_of_day) and (i.month == month) and (i.year == year)):
            print("Error! Record already exists")
            break
    else:
        #a = CalendarDay(1, 2, 3, "evening", 1, 2, 3)
        diary.append(CalendarDay(day, month, year, times_of_day, diastolic_pressure, systolic_pressure, pulse))


def is_date_valid(day, month):
    """
    Функция проверяет корректность введенного дня и месяца, их попадание в допустимый диапазон
    :param day: день, который необходимо сверить с допустимым диапазоном
    :param month: месяц, который необходимо сверить с допустимым диапазоном
    :return: корректно ли были введены день и месяц
    >>> is_date_valid(32,12)
    False
    >>> is_date_valid(12,12)
    True
    """
    a=int(day)
    b= int(month)
    if (a > 31) or (b > 12):
        return False
    else:
        return True

def is_year_valid(year):
    """
    Функция проверяет корректность введенного дня и месяца, их попадание в допустимый диапазон
    :param day: день, который необходимо сверить с допустимым диапазоном
    :param month: месяц, который необходимо сверить с допустимым диапазоном
    :return: корректно ли были введены день и месяц
    >>> is_year_valid("hgbjn")
    False
    >>> is_year_valid(2000)
    True
    """
    if year.isdigit():
      return True
    else:
      return False



def is_time_valid(times_of_day):
    """
    Функция проверяет корректность введенного времени дня
    :param times_of_day: время дня, когда было сделано измерение показателей здоровья
    :return: корректно ли было введено
    >>> is_time_valid("evening")
    True
    >>> is_time_valid("forest")
    False
    """
    reserved_part = ['morning', 'evening']
    for i in reserved_part:
        if i == times_of_day:
            return True
    else:
        return False


def is_valid_DPressure(diastolic_pressure):
    """

    :param diastolic_pressure: значение верхнего давления
    :return: корректно ли было введено значение верхнего давления
    >>> is_valid_DPressure(400)
    False
    >>> is_valid_DPressure(120)
    True
    """
    a = int(diastolic_pressure)

    if ((a >= 0) and (a <= 280)):
        return True
    else:
        return False


def is_valid_SPressure(systolic_pressure):
    """

    :param systolic_pressure: значение нижнего давления
    :return: корректно ли было введено значение нижнего давления
    >>> is_valid_SPressure(-15)
    False
    >>> is_valid_SPressure(175)
    True
    """
    b = int(systolic_pressure)
    if ((b >= 0) and (b <= 280)):
        return True
    else:
        return False


def is_pulse_norm(pulse):
    """
    Проверяет было ли введено корректно значение пульса
    :param pulse: значение пульса
    :return: корректно ли было введено значение пульса
    >>> is_pulse_norm(1000)
    False
    >>> is_pulse_norm(150)
    True
    """
    a = int(pulse)
    if ((a >= 0) and (a <= 200)):
        return True
    else:
        return False

def read_serialization_type(key1):
    # Выводит меню для выбора типа сериализации
    while True:
        if key1 == "1":
            return 'pickle'
        elif key1 == "2":
            return 'yaml'
        elif key1 == "3":
            return 'json'
        else:
            print("Wrong input! Repeat please...")
            break




def change_serialization_file(key1):
    # Считывает имя файла с которым пользователь хочет работать.
    #  Передает имя файла и его тип .
    inp = input("Enter your file name(without file format) : ")
    return read_serialization_type(key1), inp

