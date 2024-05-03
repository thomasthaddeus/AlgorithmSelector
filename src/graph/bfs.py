"""search/bfs.py
This module implements the breadth-first search (BFS) traversal algorithm for a
graph.

Breadth-first search is a graph traversal algorithm that explores all the
neighbor nodes at the present depth before moving on to nodes at the next depth
level. BFS is useful when you want to explore the nearest nodes first or when
you want to find the shortest path between two nodes. It is generally used for
problems where you want to explore a graph level by level, such as finding the
shortest path in an unweighted graph.

Ex:
g = BFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth First Traversal (starting from vertex 2):")
g.bfs(2)
"""

from collections import deque
from . import Graph


class BFS(Graph):
    """
    A class to represent the BFS traversal algorithm.

    This class inherits from the base Graph class and implements
    the BFS traversal method.
    """

    def bfs(self, start_vertex):
        """
        Perform a breadth-first traversal of the graph starting from a
        specified vertex.

        The traversal visits all nodes at the current depth before moving on to
        the next level. It uses a queue to manage the nodes that need to be
        explored.

        Args:
            start_vertex: The vertex to start the traversal from.
        """
        visited = set()
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(
                    [x for x in self.graph.get(vertex, []) if x not in visited]
                )
