import unittest
from Chapter1.Problem4.permPalindrome import pal_perm

class TestPermPalindrome(unittest.TestCase):
    def test_perm_palindrome(self):
        self.assertFalse(pal_perm("racecarf"))
        self.assertFalse(pal_perm("req"))
        self.assertTrue(pal_perm("tact coa"))
        self.assertTrue(pal_perm("godogd"))
        self.assertTrue(pal_perm(""))
