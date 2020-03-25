from unittest import TestCase
from Chapter2.Problem6.palindrome import *
from Chapter2.linked_list import *


class Test(TestCase):
    def test_palindrome(self):
        l1 = build_ll([1,2,3,2,1])
        l2 = build_ll([])
        l3 = build_ll([1,2])
        l4 = build_ll([1,2,2,1])
        l5 = build_ll([1,2,3,3,1])

        self.assertTrue(palindrome(l1))
        self.assertTrue(palindrome(l2))
        self.assertFalse(palindrome(l3))
        self.assertTrue(palindrome(l4))
        self.assertFalse(palindrome(l5))


