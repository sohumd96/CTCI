from unittest import TestCase
from Chapter3.Problem1.three_in_one import three_stack

stack = three_stack()
stack.push(1, 3)
stack.push(1, 2)
stack.push(1, 1)
stack.push(2, 3)
stack.push(2, 2)
stack.push(2, 1)
stack.push(3, 3)
stack.push(3, 2)
stack.push(3, 1)
stack.pop(1)
stack.pop(2)
stack.pop(3)
stack.pop(3)
stack.pop(3)
stack.pop(1)


class TestThreeStack(TestCase):

    def test_peek(self):
        self.assertEqual(2, stack.peek(2))
        self.assertEqual(3, stack.peek(1))

    def test_is_empty(self):
        self.assertTrue(stack.is_empty(3))

    def test_three_stack(self):
        self.assertEqual([3, None, 2, 3, None, None], stack.stack)
