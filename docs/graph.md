# Graph Algorithms

## Overview

This document is a placeholder for the summarization of the Graph algorithms and their implementations.

## Algorithms

### Bellman-Ford

1. **Bellman-Ford Overview**:
   - The algorithm is designed to handle graphs with negative-weight edges and detects negative cycles.
   - It follows a three-step process: initialization, relaxation, and cycle check.

2. **Class Design**:
   - The `BellmanFord` class represents the algorithm.
   - The `find_shortest_paths` method calculates the shortest paths from a single source and returns distances and predecessors.

3. **Error Handling**:
   - The method raises a `ValueError` if a negative-weight cycle is detected, which is important for preventing erroneous path calculations.

### Breadth-First Search

1. **BFS Overview**:
   - BFS explores the graph level by level.
   - It uses a queue to manage the nodes to be explored.

2. **Class Design**:
   - The `BFS` class inherits from the base `Graph` class, gaining common graph functionalities.
   - The `bfs` method implements the traversal logic.

3. **Docstrings**:
   - The docstrings explain the purpose of the module and its methods, along with example usage.

### Depth-First Search

1. **DFS Overview**:
   - DFS explores the graph as far as possible along each branch before backtracking.
   - It's useful for problems where you want to go deep into a graph, such as solving mazes.

2. **Class Design**:
   - The `DFS` class inherits from the base `Graph` class, gaining common graph functionalities.
   - The `dfs` method implements the traversal logic, utilizing a helper function `dfs_util`.

3. **Example Usage**:
   - The example demonstrates creating a graph, adding edges, and performing DFS traversal.

### Dijkstra

1. **Dijkstra Overview**:
   - Dijkstra's algorithm is used to find the shortest path in a graph with non-negative weights.
   - The algorithm maintains a priority queue of nodes to explore and tracks the shortest distance to each node.

2. **Class Design**:
   - The `Dijkstra` class extends the `Graph` class, allowing it to leverage shared graph functionalities.
   - The algorithm operates on a dictionary of nodes and edge weights.

3. **Docstrings**:
   - The docstrings provide an overview of the algorithm and describe the input arguments, errors, and return values.

### Kruskal

1. **Kruskal Overview**:
   - Kruskal's algorithm is a greedy algorithm used to find the MST of a graph.
   - The `Kruskal` class inherits from the base `Graph` class and focuses on implementing the algorithm.

2. **Class Design**:
   - The `DisjointSet` class helps manage subsets for union-find operations.
   - The `Kruskal` class focuses on Kruskal's algorithm, using the inherited functionalities from `Graph`.

3. **Example Usage**:
   - The example demonstrates creating a graph, adding edges, and computing the MST using Kruskal's algorithm.

### Topological Sort

1. **Topological Sort Overview**:
   - Topological sorting provides a linear ordering of vertices in a DAG.
   - It's useful for scheduling tasks with dependencies, resolving symbol dependencies, and more.

2. **Class Design**:
   - The `TopologicalSort` class inherits from the `Graph` base class.
   - The `topological_sort` method initiates the sorting, and the `topological_sort_util` method helps with the depth-first search.

3. **Example Usage**:
   - The example demonstrates creating a graph, adding edges, and performing a topological sort.
