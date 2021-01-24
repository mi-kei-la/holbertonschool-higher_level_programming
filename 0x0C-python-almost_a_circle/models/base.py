#!/usr/bin/python3
"""This module contains the Base class."""
import json


class Base():
    """This class gives all instances an id."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor, assigns ID."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of list_dictionaries.
        If list_dictionaries is empty or None, return empty list.
        """
        if list_dictionaries and len(list_dictionaries) > 0:
            if type(list_dictionaries) is not list:
                raise TypeError("argument must be list of dictionaries")
            else:
                return json.dumps(list_dictionaries)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string representation of an object to file.
        Filename is <classname>.json.
        """
        ret_list = []
        filename = cls.__name__ + ".json"
        # Check if list_objs exists, is list and is not empty.
        if list_objs and len(list_objs) > 0 and type(list_objs) is list:
            for obj in list_objs:
                if isinstance(obj, Base) is False:
                    raise TypeError("objs in list must be instance of Base")
                else:
                    obj_dic = obj.to_dictionary()
                    ret_list.append(obj_dic)
            ret_str = obj.to_json_string(ret_list)
            with open(filename, "w") as f:
                f.write(ret_str)
            return
        else:
            with open(filename, "w") as f:
                f.write(ret_list)

    @staticmethod
    def from_json_string(json_string):
        """Return the list representation of json_string.
        json_string represents a list of dictionaries.
        """
        if json_string and type(json_string) is str:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes set."""
        dummy = cls(1, 1, 1, 1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a given file."""
        filename = cls.__name__ + ".json"
        retlist = []
        try:
            with open(filename, "r") as f:
                j_string = f.read()
            dics = cls.from_json_string(j_string)
            for dic in dics:
                if type(dic) is dict:
                    obj = cls.create(**dic)
                    retlist.append(obj)
            return retlist
        except IOError:
            return []
