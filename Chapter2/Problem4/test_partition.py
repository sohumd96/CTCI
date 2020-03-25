from unittest import TestCase
from Chapter2.Problem4.partition import partition
from Chapter2.linked_list import *

class Test(TestCase):
    def test_partition(self):
        l1 = build_ll([3,5,8,5,10,2,1])
        l2 = partition(l1,5)
        self.assertEqual(get_arr(partition(l1,5)), [3,2,1,5,8,5,10])

