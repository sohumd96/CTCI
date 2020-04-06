from unittest import TestCase
from Chapter3.Problem2.stack_min import StackMin


class TestStackMin(TestCase):
    def test(self):
        stack = StackMin()
        stack.push(8)
        stack.push(5)
        stack.push(6)
        stack.push(3)
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.min(), 2)
        stack.pop()
        self.assertEqual(stack.min(), 3)
        stack.pop()
        self.assertEqual(stack.min(), 3)
        stack.pop()
        self.assertEqual(stack.min(), 5)
        stack.pop()
        self.assertEqual(stack.min(), 5)
        stack.pop()
        self.assertEqual(stack.min(), 8)
