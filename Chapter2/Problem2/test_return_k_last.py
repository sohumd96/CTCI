from unittest import TestCase
from Chapter2.linked_list import *
from Chapter2.Problem2.return_k_last import return_k_last

class Test(TestCase):
    def test_return_k_last(self):
        self.assertEqual(return_k_last(build_ll([1,2,3,4,5,6]), 4), 3)
        self.assertEqual(return_k_last(build_ll([1,2,3,4,5,6]), 1), 6)
        self.assertEqual(return_k_last(build_ll([1,2,3,4,5,6]), 1), 6)


