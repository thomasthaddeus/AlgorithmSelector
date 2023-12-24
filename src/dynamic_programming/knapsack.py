class Knapsack:
    def __init__(self, capacity, weights, values):
        self.capacity = capacity
        self.weights = weights
        self.values = values
        self.n_items = len(weights)

    def solve(self):
        """Solves the knapsack problem and returns the maximum total value."""
        dp = [[0 for _ in range(self.capacity + 1)] for _ in range(self.n_items + 1)]

        # Build table dp[][] in bottom-up manner
        for i in range(1, self.n_items + 1):
            for w in range(1, self.capacity + 1):
                if self.weights[i - 1] <= w:
                    dp[i][w] = max(self.values[i - 1] + dp[i - 1][w - self.weights[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[self.n_items][self.capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
knapsack = Knapsack(capacity, weights, values)
max_value = knapsack.solve()
print("Maximum value in the knapsack =", max_value)
