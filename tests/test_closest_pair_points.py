import unittest
from geometric.closest_pair_points import ClosestPairPoints

class TestClosestPairPoints(unittest.TestCase):
    def test_closest_pair(self):
        points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        cpp = ClosestPairPoints(points)
        self.assertEqual(cpp.find_closest_pair(), ((2, 3), (3, 4)))

if __name__ == '__main__':
    unittest.main()
