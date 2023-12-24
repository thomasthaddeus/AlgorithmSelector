import unittest
from dynamic_programming.fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        fib = Fibonacci()
        self.assertEqual(fib.recursive_fibonacci(10), 55)
        self.assertEqual(fib.dp_fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()
