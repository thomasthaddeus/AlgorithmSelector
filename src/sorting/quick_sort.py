class QuickSort:
    def __init__(self, data):
        self.data = data

    def quicksort(self, low, high):
        """Helper method to perform quicksort on the data."""
        if low < high:
            pi = self.partition(low, high)
            self.quicksort(low, pi - 1)  # Recursively sort the left subarray
            self.quicksort(pi + 1, high)  # Recursively sort the right subarray

    def partition(self, low, high):
        """Partition the array on the basis of the pivot element."""
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1

    def sort(self):
        """Public method to start the quicksort algorithm."""
        self.quicksort(0, len(self.data) - 1)

    def get_sorted_data(self):
        """Returns the sorted data."""
        return self.data

# Example usage
data = [10, 7, 8, 9, 1, 5]
quicksort = QuickSort(data)
quicksort.sort()
sorted_data = quicksort.get_sorted_data()
print("Sorted array:", sorted_data)
