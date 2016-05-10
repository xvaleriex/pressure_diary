"""config file parser module"""
from sjson import  write as json_write
#from serialization.spickle import read as pickle_read, write as pickle_write
#from serialization.sxml import read as xml_read, write as xml_write
#from serialization.syaml import read as yaml_read, write as yaml_write
import configparser


def serialize_type(fname="data/defaults.cfg"):
    """
    parse configure file
    :param fname: configure file name
    :return: functions read/write
    """
    # get configure file
    parser = configparser.ConfigParser()
    parser.read(fname)
    # get type of serialization
    type = parser['serialization']['type']
    if type == 'json':
        # JSON
        return  json_write


    else:
        # unknown type
        raise AttributeError('Incorrect serialization type')