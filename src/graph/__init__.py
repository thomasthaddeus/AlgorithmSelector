# graph/__init__.py
from collections import defaultdict

class Graph:
    """
    A base graph class that serves as a parent for other graph-related algorithms.
    """
    def __init__(self, vertices=None):
        """
        Initializes a graph with an optional set of vertices.

        Args:
            vertices: An optional list of vertices to initialize the graph with.
        """
        self.graph = defaultdict(list)
        self.vertices = vertices or []

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
            vertex: The vertex to add.
        """
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    def add_edge(self, u, v, w=None):
        """
        Adds an edge from vertex u to vertex v, optionally with a weight.

        Args:
            u: The starting vertex.
            v: The ending vertex.
            w: The optional weight of the edge.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        if w is not None:
            self.graph[u].append((v, w))
        else:
            self.graph[u].append(v)

# Now, import specific algorithm classes
from .bellman_ford import BellmanFord
from .bfs import BFS
from .dfs import DFS
from .dijkstra import Dijkstra
from .kruskal import Kruskal
from .topological_sort import TopologicalSort
