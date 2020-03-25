from unittest import TestCase
from Chapter2.linked_list import *
from Chapter2.Problem1.remove_dups import *


class Test(TestCase):
    def test_remove_dups_nobuffer(self):
        l1 = build_ll([1, 2, 3, 1, 1, 2, 1])
        l2 = build_ll([1, 2, 3, 4, 3])
        l3 = build_ll([1, 1, 1, 1])
        l4 = build_ll([1, 2, 2, 2, 2, 3])
        l5 = build_ll([1, 2, 3, 4, 2, 5, 6, 2, 4, 7, 8])

        self.assertEqual(get_arr(remove_dups_nobuffer(l1)), [1,2,3])
        self.assertEqual(get_arr(remove_dups_nobuffer(l2)), [1, 2, 3, 4])
        self.assertEqual(get_arr(remove_dups_nobuffer(l3)), [1])
        self.assertEqual(get_arr(remove_dups_nobuffer(l4)), [1, 2, 3])
        self.assertEqual(get_arr(remove_dups_nobuffer(l5)), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_remove_dups(self):
        l1 = build_ll([1, 2, 3, 1, 1, 2, 1])
        l2 = build_ll([1, 2, 3, 4, 3])
        l3 = build_ll([1, 1, 1, 1])
        l4 = build_ll([1, 2, 2, 2, 2, 3])
        l5 = build_ll([1, 2, 3, 4, 2, 5, 6, 2, 4, 7, 8])

        self.assertEqual(get_arr(remove_dups(l1)), [1, 2, 3])
        self.assertEqual(get_arr(remove_dups(l2)), [1, 2, 3, 4])
        self.assertEqual(get_arr(remove_dups(l3)), [1])
        self.assertEqual(get_arr(remove_dups(l4)), [1, 2, 3])
        self.assertEqual(get_arr(remove_dups(l5)), [1, 2, 3, 4, 5, 6, 7, 8])
