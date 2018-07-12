import unittest
from stack import stack

class TestStackMethods(unittest.TestCase):
    
    def setUp(self):
        self.stack = stack()
    
    def tearDown(self):
        while not self.stack.isEmpty:
            self.stack.pop()

    def test_empty_stack(self):
        self.assertTrue(self.stack.isEmpty())
    
    def test_size(self):
        self.assertEqual(self.stack.size(),0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(),2)

    def test_push(self):
        self.stack.push(11)
        self.assertEqual(self.stack.peek(),11)
        self.stack.push(12)
        self.stack.push(13)
        self.assertEqual(self.stack.peek(),13)
        self.assertEqual(self.stack.size(),3)
        
    def test_pop(self):
        self.stack.push(10)
        self.stack.push(11)
        self.assertEqual(self.stack.pop(),11)

if __name__=='__main__':
    unittest.main()
