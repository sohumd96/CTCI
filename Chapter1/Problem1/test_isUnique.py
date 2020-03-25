from unittest import TestCase
from Chapter1.Problem1.isUnique import isUnique1, isUnique2


class Test(TestCase):
    def testIsUnique1(self):
        self.assertFalse(isUnique1("hello"))
        self.assertTrue(isUnique1("helo"))
        self.assertTrue(isUnique1(""))
        self.assertFalse(isUnique1("helol"))

    def testIsUnique2(self):
        self.assertFalse(isUnique2("hello"))
        self.assertTrue(isUnique2("helo"))
        self.assertTrue(isUnique2(""))
        self.assertFalse(isUnique2("helol"))