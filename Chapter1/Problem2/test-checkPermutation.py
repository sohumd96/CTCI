from unittest import TestCase
from Chapter1.Problem2.checkPermutation import check_permutation

class TestCheckPermutation(TestCase):
    def test_check_permutation(self):
        self.assertTrue(check_permutation("asdf", "fasd"))
        self.assertFalse(check_permutation("", "aaa"))
        self.assertFalse(check_permutation("race", ""))
        self.assertTrue(check_permutation("popcorn", "nporopc"))