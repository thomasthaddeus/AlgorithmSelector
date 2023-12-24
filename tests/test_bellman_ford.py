import unittest
from graph_theory.bellman_ford import BellmanFord

class TestBellmanFord(unittest.TestCase):
    def test_shortest_path(self):
        graph = BellmanFord(5)
        graph.add_edge(0, 1, -1)
        graph.add_edge(0, 2, 4)
        graph.add_edge(1, 2, 3)
        graph.add_edge(1, 3, 2)
        graph.add_edge(1, 4, 2)
        graph.add_edge(3, 2, 5)
        graph.add_edge(3, 1, 1)
        graph.add_edge(4, 3, -3)
        distance = graph.bellman_ford(0)
        self.assertEqual(distance, [0, -1, 2, -2, 1])

if __name__ == '__main__':
    unittest.main()
