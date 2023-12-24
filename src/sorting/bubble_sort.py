class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        """
        Sort the data using bubble sort algorithm.
        """
        n = len(self.data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            if not swapped:
                # If no two elements were swapped in inner loop, then break
                break

    def get_sorted_data(self):
        """
        Returns the sorted data.
        """
        return self.data

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort(data)
bubble_sort.sort()
sorted_data = bubble_sort.get_sorted_data()
print("Sorted array is:", sorted_data)
