class BinarySearch:
    def __init__(self, arr):
        self.arr = sorted(arr)  # Ensuring the array is sorted

    def search(self, target):
        """Perform binary search for the target in the array."""
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = self.arr[mid]

            if mid_val == target:
                return mid  # Target found
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Target not found

# Example usage
arr = [3, 4, 5, 6, 7, 8, 9]
bs = BinarySearch(arr)
target = 5
result = bs.search(target)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
