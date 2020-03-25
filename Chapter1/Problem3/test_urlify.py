from unittest import TestCase
from Chapter1.Problem3.urlify import urlify

class Test(TestCase):
    def test_urlify(self):
        self.assertEqual(urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")
        self.assertEqual(urlify("Hello World  ", 11), "Hello%20World")
