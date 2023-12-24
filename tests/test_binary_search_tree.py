import unittest
from search.binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bs = BinarySearch(arr)
        self.assertEqual(bs.search(4), 3)
        self.assertEqual(bs.search(10), -1)

if __name__ == '__main__':
    unittest.main()
