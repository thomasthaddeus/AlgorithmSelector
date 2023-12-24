import random

class RandomizedQuickSort:
    def __init__(self, data):
        self.data = data

    def randomized_partition(self, low, high):
        """Partition the array using a randomly selected pivot."""
        pivot_index = random.randint(low, high)
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]
        return self.partition(low, high)

    def partition(self, low, high):
        """Partition the array and return the index of the pivot element."""
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1

    def quicksort(self, low, high):
        """The main QuickSort algorithm with randomization."""
        if low < high:
            pi = self.randomized_partition(low, high)
            self.quicksort(low, pi - 1)
            self.quicksort(pi + 1, high)

    def sort(self):
        """Public method to start the QuickSort algorithm."""
        self.quicksort(0, len(self.data) - 1)

    def get_sorted_data(self):
        """Returns the sorted data."""
        return self.data

# Example usage
data = [10, 7, 8, 9, 1, 5]
randomized_quick_sort = RandomizedQuickSort(data)
randomized_quick_sort.sort()
sorted_data = randomized_quick_sort.get_sorted_data()
print("Sorted array:", sorted_data)
