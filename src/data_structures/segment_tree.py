class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build_tree(arr)

    def build_tree(self, arr):
        """Builds the segment tree from the given array."""
        # Insert leaf nodes in tree
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]

        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, p, value):
        """Update value at position p in the array."""
        # Set value at position p
        p += self.n
        self.tree[p] = value

        # Move upward and update parents
        i = p
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def sum_range(self, l, r):
        """Returns the sum of the elements in the range [l, r) in the array."""
        res = 0
        l += self.n
        r += self.n

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1

        return res

# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
print("Sum of values in the range [1, 3):", seg_tree.sum_range(1, 3))
seg_tree.update(1, 10)
print("Updated sum of values in the range [1, 3):", seg_tree.sum_range(1, 3))
