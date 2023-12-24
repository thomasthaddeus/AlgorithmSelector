import unittest
from search.bfs import BFS

class TestBFS(unittest.TestCase):
    def test_traversal(self):
        graph = BFS()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        graph.add_edge(2, 3)
        graph.add_edge(3, 3)
        traversal = graph.bfs(2)
        self.assertEqual(traversal, [2, 0, 3, 1])

if __name__ == '__main__':
    unittest.main()
