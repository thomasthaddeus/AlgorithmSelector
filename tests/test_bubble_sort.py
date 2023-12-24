import unittest
from sorting.bubble_sort import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort = BubbleSort(arr)
        bubble_sort.sort()
        self.assertEqual(bubble_sort.get_sorted_data(), [11, 12, 22, 25, 34, 64, 90])

if __name__ == '__main__':
    unittest.main()
