from unittest import TestCase
from Chapter2.linked_list import *
from Chapter2.Problem5.sum_lists import sum_lists

class Test(TestCase):
    def test_sum_lists(self):
        l1 = build_ll([6,1,7])
        l2 = build_ll([2,9,5])

        self.assertEqual(get_arr(sum_lists(l1,l2)), [8,0,3,1])
