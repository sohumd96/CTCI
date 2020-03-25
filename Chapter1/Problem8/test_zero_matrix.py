from unittest import TestCase
from Chapter1.Problem8.zero_matrix import zero_matrix

class Test(TestCase):
    def test_zero_matrix(self):
        self.assertEqual(zero_matrix([[1,1,1],[1,1,0],[1,0,1]]), [[1,0,0],[0,0,0],[0,0,0]])
        self.assertEqual(zero_matrix([[0, 1, 1], [1, 1, 1], [1, 1, 1]]), [[0, 0, 0], [0, 1, 1], [0, 1, 1]])
        self.assertEqual(zero_matrix([[1, 1, 1], [0, 1, 1], [1, 1, 1]]), [[0, 1, 1], [0, 0, 0], [0, 1, 1]])
