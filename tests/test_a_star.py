import unittest
from pathfinding.a_star import AStar

class TestAStar(unittest.TestCase):
    def test_pathfinding(self):
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        a_star = AStar((0, 0), (2, 2), grid)
        path = a_star.a_star_search()
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])

if __name__ == '__main__':
    unittest.main()
