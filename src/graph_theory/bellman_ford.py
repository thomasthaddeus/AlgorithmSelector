class BellmanFord:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.distances = {}
        self.predecessors = {}

    def find_shortest_paths(self, source):
        """
        Find the shortest paths from the source to all other vertices.

        Args:
            source: The source vertex.

        Returns:
            A tuple containing two dictionaries for distances and predecessors.
        """
        # Step 1: Initialize distances from source to all vertices as infinite and distance to source itself as 0
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

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B', -1), ('A', 'C', 4), ('B', 'C', 3), ('B', 'D', 2), ('B', 'E', 2), ('D', 'B', 1), ('D', 'C', 5), ('E', 'D', -3)]
bf = BellmanFord(vertices, edges)
distances, predecessors = bf.find_shortest_paths('A')
print("Distances:", distances)
print("Predecessors:", predecessors)
