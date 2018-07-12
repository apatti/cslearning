from queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        while not self.queue.isEmpty:
            self.queue.dequeue

    def test_size(self):
        self.assertEqual(self.queue.size(),0)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.size(),1)

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(),10)
        self.queue.enqueue(11)
        self.queue.enqueue(12)
        self.assertEqual(self.queue.peek(),10)



if __name__ == '__main__':
    unittest.main()
