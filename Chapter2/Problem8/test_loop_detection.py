from unittest import TestCase
from Chapter2.linked_list import *
from Chapter2.Problem8.loop_detection import loop_detection

class Test(TestCase):
    def test_loop_detection(self):
        l1 = build_ll([1,2,3,4,5,6,7,8,9,10,11])
        get_tail(l1).next = l1.next.next.next

        self.assertEqual(loop_detection(l1).data, 4)

        l1 = build_ll([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertIsNone(loop_detection(l1))

        l1 = build_ll([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        get_tail(l1).next = l1.next.next.next.next.next

        self.assertEqual(loop_detection(l1).data, 6)
