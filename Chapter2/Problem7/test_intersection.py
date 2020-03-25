from unittest import TestCase
from Chapter2.linked_list import *
from Chapter2.Problem7.intersection import intersection

class Test(TestCase):
    def test_intersection(self):
        l1 = build_ll([1,2,3,4,5,6,7])
        l2 = build_ll([1,2,3])
        l3 = build_ll([4,5,6])
        get_tail(l1).next = l3
        get_tail(l2).next = l3

        self.assertTrue(intersection(l1,l2))

