import unittest
from search.dfs import DFS

class TestDFS(unittest.TestCase):
    def test_dfs(self):
        graph = DFS()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        graph.add_edge(2, 3)
        graph.add_edge(3, 3)
        traversal = graph.dfs(2)
        self.assertEqual(traversal, [2, 3, 0, 1])

if __name__ == '__main__':
    unittest.main()
