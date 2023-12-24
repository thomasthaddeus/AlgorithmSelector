import heapq

class AStar:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, current, goal):
        """Calculate the heuristic, typically using the Manhattan distance."""
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def get_neighbors(self, node):
        """Get neighboring nodes that can be traversed."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        neighbors = []
        for direction in directions:
            row, col = node[0] + direction[0], node[1] + direction[1]
            if 0 <= row < self.rows and 0 <= col < self.cols and not self.grid[row][col]:
                neighbors.append((row, col))
        return neighbors

    def a_star_search(self):
        """Perform A* search from start to goal."""
        open_set = []
        heapq.heappush(open_set, (0 + self.heuristic(self.start, self.goal), self.start))
        came_from = {}
        g_score = {node: float('inf') for row in self.grid for node in row}
        g_score[self.start] = 0

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == self.goal:
                return self.reconstruct_path(came_from)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score + self.heuristic(neighbor, self.goal), neighbor))

        return None

    def reconstruct_path(self, came_from):
        """Reconstruct the path from the came_from map."""
        current = self.goal
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (2, 4)
astar = AStar(start, goal, grid)
path = astar.a_star_search()
print("Path found:", path)
