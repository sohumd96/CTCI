from unittest import TestCase
from Chapter1.Problem5.oneAway import one_away

class Test(TestCase):
    def test_fun(self):
        self.assertTrue(one_away("able", "ale"))
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "bale"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("pol", "polde"))