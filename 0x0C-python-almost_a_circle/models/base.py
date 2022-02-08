#!/usr/bin/python3

"""
    Class Base
"""
import json

class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON ecoded representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string in a file
        """
        list = []
        if list_objs is None:
            list = []
        else:
            for i in list_objs:
                list.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), 'w', encoding="UTF8") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of JSON string
        """
        list = []
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionnary):
        return
