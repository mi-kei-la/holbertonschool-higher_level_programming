#!/usr/bin/python3
"""This module contains the Base class."""
import json
import csv



class Base():
    """This class gives all instances an id.

    Public attributes:
        id (int): number of instances (unless specified otherwise).

    Class methods:
        save_to_file: Write JSON string to file.
        load_from_file: Return list of instances from .json file.
        create: Return instance with attributes already set.
        save_to_file_csv: Serialize to CSV and save to .csv file.
        load_from_file_csv: Deserialize data from .csv file.

    Static methods:
        to_json_string: Return JSON representation of
                        a given list of dictionaries.
        from_json_string: Return list representation of JSON string.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor, assigns ID."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string representation of an object to file.
        Filename is <classname>.json.
        """
        ret_list = []
        filename = cls.__name__ + ".json"
        # Checks if list_objs exists, is list and is not empty. If it's
        # empty, or not a list, return an empty list.
        if list_objs and len(list_objs) > 0 and type(list_objs) is list:
            # Checks the type of all elements in list. If the element is
            # an object, then the dictionary of that element is appended
            # to a list. That list is then converted to a JSON string and
            # written to a file.
            for obj in list_objs:
                if isinstance(obj, Base) is False:
                    raise TypeError
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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        retlist = []
        # Tries to open the file and read it's contents. If the file
        # exists, the data is converted from JSON string to dictionary.
        # Each dictionary is used to create a new instance, which is
        # then added to the list that will be returned.
        try:
            with open(filename, "r") as f:
                j_string = f.read()
            dics = cls.from_json_string(j_string)
            for dic in dics:
                if type(dic) is dict:
                    obj = cls.create(**dic)
                    retlist.append(obj)
                else:
                    raise TypeError
            return retlist
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes set."""
        # Create dummy instance, then update its values.
        dummy = cls(1, 1, 1, 1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write representation of an object to CSV file.
        Filename is <classname>.csv."""
        filename = cls.__name__ + ".csv"
        # Opens file and creates a csv writer. Then for every object
        # in the list, get the dictionary, save values to a list, and
        # write list to file.
        with open(filename, "w") as fcsv:
            cwriter = csv.writer(fcsv, delimiter=",")
            for inst in list_objs:
                vals_list = []
                dic = inst.to_dictionary()
                # Appends values in the correct order.
                vals_list.append(dic["id"])
                if "width" in dic.keys():
                    vals_list.append(dic["width"])
                    vals_list.append(dic["height"])
                else:
                    vals_list.append(dic["size"])
                vals_list.append(dic["x"])
                vals_list.append(dic["y"])
                # Check if appended value is not int.
                for val in vals_list:
                    if type(val) is not int:
                        val = int(val)
                cwriter.writerow(vals_list)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        # Unless the file does not exist, opens the file and reads each row.
        # The length of the row specifies the type of object. If this is not
        # a valid value, raises a TypeError. Otherwise, values are paired
        # with their correct attribute name in a dictionary, then used to
        # create those instances. A list of instances is returned upon success
        try:
            with open(filename, "r") as fcsv:
                c_reader = csv.reader(fcsv, delimiter=",")
                retlist = []
                for row in c_reader:
                    if len(row) == 5:
                        ats = ["id", "width", "height", "x", "y"]
                    elif len(row) == 4:
                        ats = ["id", "size", "x", "y"]
                    else:
                        raise TypeError
                    values_dic = {}
                    for i in range(len(row)):
                        if type(row[i]) is not int:
                            row[i] = int(row[i])
                        values_dic[ats[i]] = row[i]
                    obj = cls.create(**values_dic)
                    retlist.append(obj)
            return retlist
        except IOError:
            raise IOError

    @staticmethod
    def from_json_string(json_string):
        """Return the list representation of json_string.
        json_string should be a list of dictionaries.
        """
        if json_string and type(json_string) is str:
            return json.loads(json_string)
        else:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.
        If list_dictionaries is empty or None, return empty list.
        """
        if list_dictionaries and len(list_dictionaries) > 0:
            if type(list_dictionaries) is not list:
                raise TypeError
            else:
                return json.dumps(list_dictionaries)
        else:
            return []
