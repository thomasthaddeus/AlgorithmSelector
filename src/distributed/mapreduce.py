from collections import defaultdict
import itertools

class MapReduce:
    def __init__(self):
        self.intermediate = defaultdict(list)
        self.result = defaultdict(list)

    def map(self, mapper, data):
        """
        Apply a mapper function to each item in the data.

        Args:
            mapper (function): A function to apply to each item.
            data (list): The data to map over.
        """
        for item in data:
            for key, value in mapper(item):
                self.intermediate[key].append(value)

    def reduce(self, reducer):
        """
        Apply a reducer function to each set of items in the intermediate data.

        Args:
            reducer (function): A function to apply to each set of items.
        """
        for key, group in self.intermediate.items():
            self.result[key] = reducer(key, group)

    def execute(self, data, mapper, reducer):
        """
        Execute the MapReduce process with the given data, mapper, and reducer.

        Args:
            data (list): The data to process.
            mapper (function): The mapper function.
            reducer (function): The reducer function.
        """
        self.map(mapper, data)
        self.reduce(reducer)
        return dict(self.result)

# Example usage
def word_count_mapper(document):
    for word in document.split():
        yield (word, 1)

def word_count_reducer(word, counts):
    return sum(counts)

documents = ["hello world", "world hello", "hello world world"]

map_reduce = MapReduce()
word_counts = map_reduce.execute(documents, word_count_mapper, word_count_reducer)

print(word_counts)
