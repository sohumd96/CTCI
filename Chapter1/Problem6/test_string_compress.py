from unittest import TestCase
from Chapter1.Problem6.string_compress import compress

class Test(TestCase):
    def test_compress(self):
        self.assertEqual(compress("aaabcdd"), "a3b1c1d2")
        self.assertEqual(compress("yyyyyaahhhhkk"), "y5a2h4k2")
        self.assertEqual(compress("ttttorrrrrrrqq"), "t4o1r7q2")
