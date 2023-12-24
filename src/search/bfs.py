from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start_vertex):
        """Perform BFS starting from start_vertex."""
        visited = set()
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend([x for x in self.graph.get(vertex, []) if x not in visited])

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth First Traversal (starting from vertex 2)")
g.bfs(2)
