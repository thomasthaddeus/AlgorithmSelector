class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in vertices}
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
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

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal_mst(self):
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

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
g = Graph(vertices)
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
