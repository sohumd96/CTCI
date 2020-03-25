from unittest import TestCase
from Chapter1.Problem9.string_rotation import string_rotation

class Test(TestCase):
    def test_string_rotation(self):
        self.assertTrue(string_rotation("waterbottle", "erbottlewat"))
        self.assertTrue(string_rotation("racecar", "carrace"))
        self.assertFalse(string_rotation("dog", "god"))
