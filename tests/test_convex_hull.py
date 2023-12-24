import unittest
from geometric.convex_hull import ConvexHull

class TestConvexHull(unittest.TestCase):
    def test_convex_hull(self):
        points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
        ch = ConvexHull(points)
        hull = ch.compute_convex_hull()
        expected_hull = [(0, 0), (3, 0), (3, 3), (0, 3)]
        self.assertEqual(hull, expected_hull)

if __name__ == '__main__':
    unittest.main()
