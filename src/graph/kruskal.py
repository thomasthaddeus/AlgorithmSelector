"""
This module implements Kruskal's algorithm for finding the Minimum Spanning
Tree (MST) of a graph.

Kruskal's algorithm is a greedy algorithm that finds an MST for a connected,
weighted, undirected graph. It works by sorting all the edges in ascending
order by weight and then adding them one by one to the MST, ensuring that no
cycles are formed. The algorithm uses a Disjoint Set data structure to keep
track of which nodes belong to which subset.

This implementation includes:
1. A `DisjointSet` class to manage subsets and perform union-find operations.
2. A `Kruskal` class that inherits from the base `Graph` class and provides
   methods to add edges and compute the MST.

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
g = Kruskal(vertices)
g.add_edge('A', 'B', 4)
g.add_edge('A', 'F', 2)
g.add_edge('F', 'B', 5)
g.add_edge('C', 'B', 6)
g.add_edge('C', 'F', 1)
g.add_edge('F', 'E', 4)
g.add_edge('E', 'D', 2)
g.add_edge('D', 'C', 3)

mst = g.kruskal_mst()
print("Minimum Spanning Tree:", mst)
"""

from . import Graph


class DisjointSet:
    """
    A class to represent a disjoint set for union-find operations.

    The `DisjointSet` class helps manage subsets of elements and supports the
    union and find operations, which are used to check if two elements belong
    to the same subset.
    """


    def __init__(self, vertices):
        """
        Initializes the disjoint set with the given vertices.

        Args:
            vertices: A list of vertices to initialize the disjoint set with.
        """
        self.parent = {v: v for v in vertices}
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        """
        Finds the root of the set containing the given item.

        This function uses path compression to improve efficiency.

        Args:
            item: The item to find the set for.

        Returns:
            The root of the set containing the item.
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Performs the union of the sets containing x and y.

        This function uses union by rank to improve efficiency.

        Args:
            x: An element in the first set.
            y: An element in the second set.
        """
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

class Kruskal(Graph):
    """
    A class to implement Kruskal's algorithm using the base Graph class.

    The `Kruskal` class inherits from the base Graph class and allows for
    finding the Minimum Spanning Tree using Kruskal's algorithm.
    """

    def add_edge(self, u, v, w=None):
        """
        Adds an edge to the graph.

        Args:
            u: The starting vertex of the edge.
            v: The ending vertex of the edge.
            w: The weight of the edge.
        """
        super().add_edge(u, v, w)
        self.graph.append([u, v, w])

    def kruskal_mst(self):
        """
        Finds the Minimum Spanning Tree (MST) using Kruskal's algorithm.

        The algorithm sorts all the edges by weight and adds them one by one to
        the MST, ensuring that no cycles are formed using the Disjoint Set data
        structure.

        Returns:
            list: A list of edges included in the MST.
        """
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        ds = DisjointSet(self.vertices)

        while e < len(self.vertices) - 1:
            u, v, w = self.graph[i]
            i += 1
            x = ds.find(u)
            y = ds.find(v)
            if x != y:
                e += 1
                result.append([u, v, w])
                ds.union(x, y)

        return result
