class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph  # Residual graph
        self.ROW = len(graph)

    def searching_algorithm(self, source, sink, parent):
        """Function to implement searching algorithm (like BFS) to find path from source to sink."""
        visited = [False] * self.ROW
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[sink] else False

    def ford_fulkerson(self, source, sink):
        """Returns the maximum flow from source to sink in the given graph."""
        parent = [-1] * self.ROW
        max_flow = 0

        while self.searching_algorithm(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # Update residual capacities of the edges and reverse edges along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Example usage
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5

ford_fulkerson_solver = FordFulkerson(graph)
print("Maximum Flow: ", ford_fulkerson_solver.ford_fulkerson(source, sink))
