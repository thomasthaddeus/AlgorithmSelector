"""search/dfs.py
This module implements depth-first search (DFS) for a graph.

Depth-first search is a graph traversal algorithm that explores as far as
possible along each branch before backtracking. It is often used when you want
to visit all nodes in a graph or when you want to find a path to a specific
node. DFS is better than breadth-first search (BFS) for problems where you want
to search deep into a graph, such as solving mazes or puzzles, where the
solution might be closer to a certain starting point.

The main advantage of DFS over BFS is that it requires less memory, as it
explores one branch at a time, making it more efficient when the solution is
deep in the graph. BFS, on the other hand, is better for finding the shortest
path between two nodes.

# Example usage
g = DFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2)
"""

from . import Graph

class DFS(Graph):
    """
    A class to represent the DFS traversal algorithm.

    This class inherits from the base Graph class and implements
    the DFS traversal method.
    """
    def dfs_util(self, v, visited):
        """
        A utility function for DFS traversal.

        This function is a helper for the main DFS function.
        It recursively visits all the nodes connected to node v.

        Args:
            v: The node to start the traversal from.
            visited: A set to keep track of visited nodes.
        """
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        """
        Perform a depth-first traversal of the graph starting from a specified
        vertex.

        The traversal explores as far as possible along each branch before
        backtracking.

        Args:
            v: The starting vertex for the traversal.
        """
        visited = set()
        self.dfs_util(v, visited)
