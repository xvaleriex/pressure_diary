import unittest
from Menu import *
from Pickle_file import *
from Json_file import *
from Yaml_file import *
from Structure import *
class TestSerialization(unittest.TestCase):

    def create_user(self):
        usr = CalendarDay(2, 3, 2009,'evening', 163, 121, 89 )
        usr.getList()
        usr.self_print()
        usr.setNewTimes_of_day("evening")
        usr.setNewDiastolic_pressure(163)
        usr.setNewSystolic_pressure(121)
        usr.setNewPulse(89)
        getAllRecords()
        CreateRecord(9,9,2009,"morning",65,60,45)
        is_date_valid(32,12)
        is_date_valid(12,12)
        is_valid_DPressure(400)
        is_valid_DPressure(120)
        is_valid_SPressure(-15)
        is_valid_SPressure(175)
        is_pulse_norm(1000)
        is_pulse_norm(150)
        read_serialization_type("1")
        Main_menu()
        Date_menu()
        File_menu()
        #user_input()
        show_tip("hello")
        #displayDayInfo()
        #change_serialization_file("1")
        return usr

    def test_pickle(self):
     # Функция для тестирования модуля pickle
        obj = self.create_user()
        Pickle('test_pickle').dump(obj)
        obj1 = Pickle('test_pickle').loading_f()
        for p1, p2 in zip([obj.day], [obj1.day]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.month], [obj1.month]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.year], [obj1.year]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.times_of_day], [obj1.times_of_day]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.diastolic_pressure], [obj1.diastolic_pressure]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.systolic_pressure], [obj1.systolic_pressure]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.pulse], [obj1.pulse]):
            self.assertEqual(p1, p2)


    def test_yaml(self):
        # Функция для тестирования модуля yaml
        obj = self.create_user()
        Yaml('test_yaml').dump(obj)
        obj1 = Yaml('test_yaml').loading_f()
        for p1, p2 in zip([obj.day], [obj1.day]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.month], [obj1.month]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.year], [obj1.year]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.times_of_day], [obj1.times_of_day]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.diastolic_pressure], [obj1.diastolic_pressure]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.systolic_pressure], [obj1.systolic_pressure]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.pulse], [obj1.pulse]):
            self.assertEqual(p1, p2)


    def test_json(self):

        # Функция тестирования модуля json
        obj = self.create_user()
        temp = []
        temp.append(obj)
        Json('test_json').write(run(temp))
        flag = "2"
        obj1 = Json('test_json').read(flag)
        for p1, p2 in zip([obj.day], [obj1.day]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.month], [obj1.month]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.year], [obj1.year]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.times_of_day], [obj1.times_of_day]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.diastolic_pressure], [obj1.diastolic_pressure]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.systolic_pressure], [obj1.systolic_pressure]):
            self.assertEqual(p1, p2)
        for p1, p2 in zip([obj.pulse], [obj1.pulse]):
            self.assertEqual(p1, p2)




if __name__ == '__main__':
    unittest.main()