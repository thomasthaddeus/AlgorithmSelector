import unittest
from graph.dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        graph = Dijkstra(5)
        graph.add_edge(0, 1, 4)
        graph.add_edge(0, 2, 1)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 2)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 4, 4)
        shortest_path = graph.dijkstra(0)
        self.assertEqual(shortest_path, [0, 3, 1, 5, 7])

if __name__ == '__main__':
    unittest.main()
