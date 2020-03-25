from unittest import TestCase
from Chapter2.linked_list import *
from Chapter2.Problem3.delete_middle import delete_middle

class Test(TestCase):
    def test_delete_middle(self):
        l1 = build_ll([1,2,3,4,5])
        delete_middle(l1.next.next)
        self.assertEqual(get_arr(l1), [1,2,4,5])

        l2 = build_ll([1, 2, 3, 4, 5])
        delete_middle(l2.next.next.next)
        self.assertEqual(get_arr(l2), [1, 2, 3, 5])

