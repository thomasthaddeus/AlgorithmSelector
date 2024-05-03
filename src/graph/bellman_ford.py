"""graph/bellman_ford.py
The Bellman-Ford algorithm is an algorithm for finding the shortest paths from
a single source to all other vertices in a graph. Unlike Dijkstra's algorithm,
Bellman-Ford can handle negative-weight edges, which makes it useful for
certain problems where such edges exist.

The algorithm works in three main steps:
1. Initialization: Set the distance from the source to all vertices as
   infinite, except the source itself, which is set to zero.
2. Relaxation: Relax all edges |V| - 1 times, where V is the number of
   vertices. This means repeatedly updating the shortest known distance to each
   vertex.
3. Cycle Check: Check for negative-weight cycles by examining if any further
   relaxation is possible.

The algorithm is useful when you need to consider graphs with negative weights or when you want to detect negative cycles.

Raises:
    ValueError: If the graph contains a negative-weight cycle.

Returns:
    tuple: A tuple containing two dictionaries. The first dictionary maps
    vertices to their shortest distances from the source, and the second
    dictionary maps each vertex to its predecessor on the shortest path.

Ex:
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', -1),
    ('A', 'C', 4),
    ('B', 'C', 3),
    ('B', 'D', 2),
    ('B', 'E', 2),
    ('D', 'B', 1),
    ('D', 'C', 5),
    ('E', 'D', -3)
]
bf = BellmanFord(vertices, edges)
distances, predecessors = bf.find_shortest_paths('A')
print(f"Distances: {distances}\nPredecessors: {predecessors}")
"""

from . import Graph


class BellmanFord(Graph):
    """
    A class to represent the Bellman-Ford algorithm.

    The Bellman-Ford algorithm computes the shortest paths from a single source
    to all other vertices in a graph, even when negative weights are present.
    """
    def __init__(self, vertices, edges):
        super().__init__(vertices)
        self.edges = edges
        self.distances = {}
        self.predecessors = {}

    def find_shortest_paths(self, source):
        """
        Finds the shortest paths from the source to all other vertices.

        The function uses the Bellman-Ford algorithm to compute the shortest
        paths and detects any negative-weight cycles.

        Args:
            source: The source vertex.

        Returns:
            tuple: A tuple containing two dictionaries for distances and predecessors.

        Raises:
            ValueError: If the graph contains a negative-weight cycle.
        """
        # Step 1: Initialize distances from source to all vertices as infinite
        #         and distance to source itself as 0
        for vertex in self.vertices:
            self.distances[vertex] = float('inf')
            self.predecessors[vertex] = None
        self.distances[source] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(len(self.vertices) - 1):
            for u, v, w in self.edges:
                if self.distances[u] != float('inf') and self.distances[u] + w < self.distances[v]:
                    self.distances[v] = self.distances[u] + w
                    self.predecessors[v] = u

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.edges:
            if self.distances[u] != float('inf') and self.distances[u] + w < self.distances[v]:
                raise ValueError("Graph contains a negative-weight cycle")

        return self.distances, self.predecessors
