class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store graph

    def add_edge(self, u, v):
        """Add an edge to the graph."""
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs_util(self, v, visited):
        """A utility function for DFS traversal."""
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        """The DFS traversal of the vertices."""
        visited = set()
        self.dfs_util(v, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2)
