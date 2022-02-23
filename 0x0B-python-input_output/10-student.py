#!/usr/bin/python3
"""
Module for class student
"""


class Student():
    """
        class Student
    """
    def __init__(self, first_name, last_name, age):
        """
            init
            Args:
                first_name: first name of student
                last_name: last name of student
                age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            returns a dictionnary version of student
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return(self.__dict__)