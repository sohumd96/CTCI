from unittest import TestCase
from Chapter3.Problem3.set_of_stacks import SetOfStacks


class TestSetOfStacks(TestCase):
    def test_set_of_stacks(self):
        stack = SetOfStacks(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)
        stack.push(8)
        self.assertEqual(stack.stack_set, [[1, 2, 3], [4, 5, 6], [7, 8]])
        stack.pop_at(0)
        self.assertEqual(stack.stack_set, [[1, 2, 4], [5, 6, 7], [8]])
        stack.pop_at(1)
        self.assertEqual(stack.stack_set, [[1, 2, 4], [5, 6, 8]])
