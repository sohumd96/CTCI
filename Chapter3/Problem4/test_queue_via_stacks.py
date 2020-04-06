from unittest import TestCase
from Chapter3.Problem4.queue_via_stacks import Queue

class TestQueue(TestCase):
    def test_set_of_stacks(self):
        q1 = Queue()
        q1.enqueue(3)
        q1.enqueue(4)
        q1.enqueue(5)
        q1.enqueue(6)
        self.assertEqual(q1.dequeue(), 3)
        q1.enqueue(7)
        q1.enqueue(8)
        self.assertEqual(q1.dequeue(), 4)
        self.assertEqual(q1.dequeue(), 5)
        self.assertEqual(q1.dequeue(), 6)
        self.assertEqual(q1.dequeue(), 7)
        self.assertEqual(q1.dequeue(), 8)
        self.assertIsNone(q1.dequeue())
