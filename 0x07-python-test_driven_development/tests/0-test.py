#!/usr/bin/python3
""" Test module """

import unittest
add_integer = __import__('0-add_integer').add_integer

class test_add_integer(unittest.TestCase):
    def test_add_int1(self):
        n = add_integer(7, 8)
        self.assertEquals(n, 15)
    def test_add_int2(self):
        n = add_integer("a", 5)
        self.assertRaises()