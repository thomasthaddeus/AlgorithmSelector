"""graph/topological_sort.py
This module implements topological sorting for a directed acyclic graph (DAG).

Topological sorting is a linear ordering of vertices such that for every directed edge
from vertex u to vertex v, u comes before v in the ordering. It's often used in scenarios
where you want to schedule tasks that have dependencies on each other.

Topological sorting is only possible for DAGs because it ensures no cycles exist, which
would otherwise prevent a linear ordering. It’s useful for task scheduling, resolving
symbol dependencies in linkers, and determining compilation order.

Returns:
    list: A list of vertices in topologically sorted order.

# Example usage:
g = TopologicalSort(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
print(g.topological_sort())
"""

from collections import defaultdict
from . import Graph


class TopologicalSort(Graph):
    """
    A class to represent topological sorting for a directed acyclic graph (DAG).

    The `TopologicalSort` class inherits from the base `Graph` class and allows
    for topologically sorting the vertices in a DAG.
    """
    def __init__(self, vertices):
        """
        Initializes the graph with the given number of vertices.

        Args:
            vertices: The number of vertices in the graph.
        """
        super().__init__(vertices)
        self.V = vertices

    def add_edge(self, u, v):
        """
        Adds a directed edge from vertex u to vertex v.

        Args:
            u: The starting vertex of the edge.
            v: The ending vertex of the edge.
        """
        super().add_edge(u, v, w=None)

    def topological_sort_util(self, v, visited, stack):
        """
        A utility function for topological sorting.

        This function performs a depth-first search on the graph and inserts
        vertices into the stack in reverse post-order.

        Args:
            v: The current vertex being processed.
            visited: A list to keep track of visited vertices.
            stack: A list to maintain the topological ordering.
        """
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        """
        Performs topological sorting on the graph.

        This function initiates the topological sorting of the vertices.

        Returns:
            list: A list of vertices in topologically sorted order.
        """
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack
