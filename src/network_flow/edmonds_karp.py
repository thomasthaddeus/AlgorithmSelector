from collections import deque

class EdmondsKarp:
    def __init__(self, capacity, source, sink):
        self.capacity = capacity
        self.source = source
        self.sink = sink
        self.parent = {}
        self.n = len(capacity)

    def bfs(self):
        """Breadth-first search to find the shortest augmenting path."""
        self.parent = {self.source: None}
        queue = deque([self.source])
        while queue:
            u = queue.popleft()
            for v in range(self.n):
                if v not in self.parent and self.capacity[u][v] - self.flow[u][v] > 0:
                    self.parent[v] = u
                    queue.append(v)
                    if v == self.sink:
                        return True
        return False

    def max_flow(self):
        """Calculate the maximum flow from source to sink."""
        self.flow = [[0] * self.n for _ in range(self.n)]
        max_flow = 0
        while self.bfs():
            path_flow = float('inf')
            s = self.sink
            while s != self.source:
                path_flow = min(path_flow, self.capacity[self.parent[s]][s] - self.flow[self.parent[s]][s])
                s = self.parent[s]
            max_flow += path_flow
            v = self.sink
            while v != self.source:
                u = self.parent[v]
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                v = self.parent[v]
        return max_flow

# Example usage
capacity = [[0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5

edmonds_karp_solver = EdmondsKarp(capacity, source, sink)
print("Maximum Flow:", edmonds_karp_solver.max_flow())
