class MergeSort:
    def __init__(self, data):
        self.data = data

    def merge_sort(self, data):
        """Helper method to perform the merge sort algorithm."""
        if len(data) > 1:
            mid = len(data) // 2
            L = data[:mid]
            R = data[mid:]

            self.merge_sort(L)  # Sorting the first half
            self.merge_sort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1

    def sort(self):
        """Public method to start the merge sort algorithm."""
        self.merge_sort(self.data)

    def get_sorted_data(self):
        """Returns the sorted data."""
        return self.data

# Example usage
data = [12, 11, 13, 5, 6, 7]
merge_sort = MergeSort(data)
merge_sort.sort()
sorted_data = merge_sort.get_sorted_data()
print("Sorted array is:", sorted_data)
