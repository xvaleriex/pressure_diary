import yaml


class Yaml:

    def __init__(self, file_name):
        self.file_name = file_name


    def dump(self, data):
        # Загружает данные в файл
        with open(self.file_name + '.yaml', 'wt') as f:
            yaml.dump(data, f)

     
    def loading_f(self):
        #Считывает информацию с файла.
        # В случае отсутствия заданого файла выдает ошибку.
        try:
            with open(self.file_name + '.yaml', 'rt') as f:
                return yaml.load(f)
        except IOError:
            print('File not found')