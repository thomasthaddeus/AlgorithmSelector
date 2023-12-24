import unittest
from sorting.quick_sort import QuickSort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        quick_sort = QuickSort(arr)
        quick_sort.sort()
        self.assertEqual(arr, [1, 1, 2, 3, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()