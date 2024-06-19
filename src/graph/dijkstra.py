"""graph/dijkstra.py
This module implements Dijkstra's algorithm for finding the shortest path in a
graph.

Dijkstra's algorithm is a popular algorithm used to solve the single-source
shortest path problem for a graph with non-negative edge weights. It computes
the shortest path from a source node to a target node or all other nodes. The
algorithm maintains a priority queue of nodes to explore and keeps track of the
shortest distance found to each node.

The algorithm is useful when you need to determine the shortest or least costly
path between nodes in a graph, such as in routing and logistics applications.

Raises:
    ValueError: If the input graph is not valid or if the start or end node is
    not in the graph.

Returns:
    tuple: A tuple containing two dictionaries for distances and predecessors.

# Example usage:
# graph_data = {
#     'A': {'B': 10, 'C': 20},
#     'B': {'D': 15},
#     'C': {'D': 30, 'E': 5},
#     'D': {'E': 10},
#     'E': {}
# }
# dijkstra = Dijkstra(graph_data)
# dijkstra.print_path('A', 'E')
"""

from typing import Dict, Optional
from . import Graph

class Dijkstra(Graph):
    """
    Encapsulates Dijkstra's algorithm for finding the shortest path in a graph.

    The graph is represented as a dictionary where each key is a node, and the
    value is another dictionary representing the neighboring nodes and the cost
    to reach them.
    """

    def __init__(self, graph: Dict[str, Dict[str, int]]):
        """
        Initializes the Dijkstra class with a given graph.

        Args:
            graph: The graph in which to find the shortest path.

        Raises:
            ValueError: If the input graph is not valid.
        """
        super().__init__(vertices=list(graph.keys()))
        self.graph = graph
        self.infinity = float("inf")
        self.costs = {}
        self.parents = {}
        self.processed = []

    def initial_costs_parents(self, start: str):
        """
        Initializes the costs and parents dictionaries for the start of the
        algorithm.

        Args:
            start: The node from which to start the search.

        Raises:
            ValueError: If the start node is not in the graph.
        """
        if start not in self.graph:
            raise ValueError("Start node must be in the graph.")

        for node in self.graph:
            self.costs[node] = 0 if node == start else self.infinity
            self.parents[node] = None

    def find_lowest_cost_node(self, costs: Dict[str, int]) -> Optional[str]:
        """
        Finds the unprocessed node with the lowest known cost.

        Args:
            costs: A dictionary of the current cost to reach each node.

        Returns:
            Optional[str]: The unprocessed node with the lowest known cost, or
            None.
        """
        lowest_cost = self.infinity
        lowest_cost_node = None
        for node in costs:
            if costs[node] < lowest_cost and node not in self.processed:
                lowest_cost, lowest_cost_node = costs[node], node
        return lowest_cost_node

    def find_shortest_path(self, start: str, end: str):
        """
        Applies Dijkstra's algorithm to find the shortest path in the graph.

        Args:
            start: The node from which to start the search.
            end: The node to which to find the path.

        Raises:
            ValueError: If the start or end node is not in the graph.
        """
        if start not in self.graph or end not in self.graph:
            raise ValueError("Both start and end nodes must be in the graph.")

        self.initial_costs_parents(start)
        node = start
        while node is not None:
            self.processed.append(node)
            cost = self.costs[node]
            for neighbor, weight in self.graph[node].items():
                new_cost = cost + weight
                if new_cost < self.costs[neighbor]:
                    self.costs[neighbor], self.parents[neighbor] = new_cost, node
            node = self.find_lowest_cost_node(self.costs)

    def print_path(self, start: str, end: str):
        """
        Prints the shortest path from start node to end node.

        Args:
            start: The start node of the path.
            end: The end node of the path.
        """
        self.find_shortest_path(start, end)
        path, node = [], end
        while node:
            path.append(node)
            node = self.parents.get(node)
        if path[-1] != start:
            print(f"No path from {start} to {end}")
        else:
            print(f"Shortest path from {start} to {end}: {path[::-1]}")
