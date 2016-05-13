import json

from Structure import *


class Json:

    def __init__(self, file_name):
        self.file_name = file_name


    def read(self,flag):
        #Считывает информацию с файла.
        # В случае отсутствия заданого файла выдает ошибку.
        try:
            with open(self.file_name + '.json', 'rt') as file:

                return transform(json.load(file),flag)
        except IOError:
            print ("File not found")

    def write(self,obj ):
        # Загружает данные в файл
        if not isinstance(obj, list):

            raise ValueError('Incorrect type of variable obj')
        with open(self.file_name + '.json', 'wt') as file:
            json.dump(obj , file,  indent=4)
        file.close()

def transform(dict,flag):
    #В виде аргумента функция получает словарь . Создаем обьект класса CalendarDay()
    # и записываем в него соответствующие значения из словаря.

        ret_data = CalendarDay(3, 4, 5 ,"evening" ,122, 121 ,33)
        i = 0
        list_o=[]
        while i < len(dict):
            ret_data.day= dict[i]["day"]
            ret_data.month = dict[i]["month"]
            ret_data.year = dict[i]["year"]
            ret_data.times_of_day = dict[i]["times_of_day"]
            ret_data.diastolic_pressure = dict[i]["diastolic_pressure"]
            ret_data.systolic_pressure = dict[i]["systolic_pressure"]
            ret_data.pulse = dict[i]["pulse"]
            list_o.append(ret_data)
            i=i+1
        if flag == "1" :
            return list_o
        else :
         return ret_data

