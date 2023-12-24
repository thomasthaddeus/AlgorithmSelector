#!/bin/bash

# Define the project root and src directory
PROJECT_ROOT="my_algorithm_project"
SRC_DIR="$PROJECT_ROOT/my_algorithm_project"

# Create project root directory
mkdir -p "$SRC_DIR"

# Create base algorithm file
echo "Creating base algorithm file..."
touch "$SRC_DIR/algorithm_base.py"

# List of algorithms
ALGORITHMS=("bubble_sort" "merge_sort" "quick_sort" "binary_search" "dfs" "bfs"
            "dijkstra" "kruskal" "fibonacci" "knapsack" "linear_regression"
            "k_means" "rsa" "aes" "kmp" "rabin_karp" "newton_raphson" "euclidean"
            "huffman_coding" "lzw_compression" "a_star" "binary_search_tree"
            "avl_tree" "segment_tree" "convex_hull" "line_intersection"
            "closest_pair_points" "minimax" "nash_equilibrium" "ford_fulkerson"
            "edmonds_karp" "sweep_line" "polygon_triangulation" "topological_sort"
            "bellman_ford" "monte_carlo" "randomized_quicksort" "heap" "trie"
            "sieve_of_eratosthenes" "fast_fourier_transform" "simulated_annealing"
            "genetic_algorithm" "boyer_moore" "tf_idf" "canny_edge_detector"
            "hough_transform" "paxos" "raft" "mapreduce" "shor" "grover")

# Create files for each algorithm
for algo in "${ALGORITHMS[@]}"; do
    echo "Creating file for $algo..."
    touch "$SRC_DIR/${algo}.py"
done

# Create test directory and test files
TEST_DIR="$PROJECT_ROOT/tests"
mkdir -p "$TEST_DIR"

for algo in "${ALGORITHMS[@]}"; do
    echo "Creating test file for $algo..."
    touch "$TEST_DIR/test_${algo}.py"
done

echo "Project structure created successfully!"
