class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert_key(self, key):
        """Inserts a new key into the heap."""
        self.heap.append(key)
        i = len(self.heap) - 1
        # Fix the min heap property if it is violated
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def min_heapify(self, i):
        """A recursive method to heapify a subtree with the root at given index."""
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def extract_min(self):
        """Extracts the root which is the minimum element of the heap."""
        if len(self.heap) <= 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_heapify(0)
        return root

# Example usage
min_heap = MinHeap()
min_heap.insert_key(3)
min_heap.insert_key(2)
min_heap.insert_key(15)
min_heap.insert_key(5)
min_heap.insert_key(4)
min_heap.insert_key(45)

print("Extracted minimum:", min_heap.extract_min())
