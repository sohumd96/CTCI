from unittest import TestCase
from Chapter3.Problem5.sort_stack import SortStack

class TestSortStack(TestCase):
    def test_sort_stack(self):
        sort_stack = SortStack()
        sort_stack.push(2)
        sort_stack.push(3)
        sort_stack.push(4)
        sort_stack.push(5)
        self.assertEqual(sort_stack.peek(), 2)
        self.assertEqual(sort_stack.pop(), 2)
        sort_stack.push(3)
        self.assertEqual(sort_stack.peek(), 3)
        sort_stack.push(8)
        self.assertEqual(sort_stack.peek(), 3)
