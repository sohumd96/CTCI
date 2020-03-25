from unittest import TestCase
from Chapter1.Problem7.rotate_matrix import rotate_matrix

class Test(TestCase):
    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]),
                         [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])
        self.assertEqual(rotate_matrix([[1,2],[3,4]]), [[3,1],[4,2]])
        self.assertEqual(rotate_matrix([[1,2,3],[3,4,5],[6,7,8]]), [[6,3,1],[7,4,2],[8,5,3]])
