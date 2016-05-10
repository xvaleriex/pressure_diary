import configparser
from Pickle_file import Pickle
from Json_file import *

from Yaml_file import *
import Menu
import Structure


class Serialize:

    def __init__(self):
        self.parser = configparser.ConfigParser()

    @staticmethod
    def change_config(serialization_type, filename):
        cfgfile = open("config.ini", 'w')
        config = configparser.ConfigParser()
        if not config.has_section('serialization'):
            config.add_section('serialization')
        config.set('serialization', 'name', serialization_type)
        config.set('serialization', 'filename', filename)
        config.write(cfgfile)
        cfgfile.close()



    def read_config(self):
        try:
            self.parser.read('config.ini')
            return self.parser.get('serialization', 'name'),\
                self.parser.get('serialization', 'filename')
        except configparser.ParsingError :
            print ('Could not parse:')



    def load(self):
        # Функция ,в зависимости от выбраного пользователем вида файла,
        #  вызывает соответствующую функцию чтения из файла
        serial = self.read_config()

        flag = "1"
        if serial[0] == 'pickle':
            Structure.diary = Pickle(serial[1]).loading_f()

        elif serial[0] == "json":
            Structure.diary =  Json(serial[1]).read(flag)
        elif serial[0] == "yaml":
            Structure.diary =  Yaml(serial[1]).loading_f()

    def dump(self, data):
        # Функция ,в зависимости от выбраного пользователем вида файла,
        #  вызывает соответствующую функцию загрузки в файл .
        serial = self.read_config()
        if serial[0] == 'pickle':
            return Pickle(serial[1]).dump(data)
        elif serial[0] == "json":
            return Json(serial[1]).write(data)
        elif serial[0] == "yaml":
            return Yaml(serial[1]).dump(data)
