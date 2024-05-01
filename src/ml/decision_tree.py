"""decision_tree.py

DecisionTree: A class to build and visualize a decision tree for classification.

Example:
>>> dt = DecisionTree()
>>> cars = dt.make_cars()
>>> random.shuffle(cars)
>>> cars = cars[:1000]
>>> car_data = [x[:-1] for x in cars]
>>> car_labels = [x[-1] for x in cars]
>>> tree = dt.build_tree(car_data, car_labels)
>>> dt.print_tree(tree)

leaf_instance = DecisionTree.Leaf(labels, some_value)
decision_node_instance = DecisionTree.Decision_Node(some_question, some_branches, some_value)

"""

from collections import Counter, namedtuple
import random


class DecisionTree:
    """
    A class that represents a decision tree for classification.

    This class provides methods to build and visualize a decision tree
    based on the Gini impurity and information gain metrics.

    Attributes:
        data (list): The dataset used to build the decision tree.
    """

    _leaf = namedtuple("_leaf", ["predictions", "value"])
    _decision_node = namedtuple(
        "_decision_node", ["question", "branches", "value"]
    )

    def __init__(self, filename="car.data"):
        """
        Initializes the DecisionTree with data from a given filename.

        Args:
            filename (str): The name of the file containing the data. Defaults
                to "car.data".
        """
        self.data = self.make_cars(filename)
        random.seed(1)

    @classmethod
    def leaf(cls, labels, value):
        """
        Creates a leaf node for the decision tree.

        Args:
            labels (list): The labels associated with the data at this leaf.
            value (str): The value of the current node.

        Returns:
            namedtuple: A named tuple representing the leaf node.
        """
        predictions = Counter(labels)
        return cls._leaf(predictions, value)

    @classmethod
    def decision_node(cls, question, branches, value):
        """
        Creates a decision node for the decision tree.

        Args:
            question (int): The column index of the feature/question.
            branches (list): The branches stemming from this decision node.
            value (str): The value of the current node.

        Returns:
            namedtuple: A named tuple representing the decision node.
        """
        return cls._decision_node(question, branches, value)

    def make_cars(self, filename):
        """
        Reads data from a file and returns it as a list of lists.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            list: A list of lists where each inner list represents a data row.
        """
        with open(filename, mode="r", encoding="utf-8") as f:
            return [line.rstrip().split(",") for line in f]

    def split(self, dataset, labels, column):
        """
        Splits the dataset and labels based on unique values in a specified
          column.

        Args:
            dataset (list): The dataset to split.
            labels (list): The labels corresponding to the dataset.
            column (int): The column index based on which to split the dataset.

        Returns:
            tuple: Two lists - one containing subsets of the dataset and the
              other containing subsets of labels.
        """
        data_subsets = []
        label_subsets = []
        counts = sorted(set(data[column] for data in dataset))

        for k in counts:
            new_data_subset = [
                data for _, data in enumerate(dataset) if data[column] == k
            ]
            new_label_subset = [
                i for _, i in enumerate(labels) if dataset[_][column] == k
            ]
            data_subsets.append(new_data_subset)
            label_subsets.append(new_label_subset)

        return data_subsets, label_subsets

    def gini(self, dataset):
        """
        Calculates the Gini impurity of a dataset.

        Args:
            dataset (list): The dataset for which to calculate the Gini
              impurity.

        Returns:
            float: The Gini impurity of the dataset.
        """
        impurity = 1
        label_counts = Counter(dataset)
        for label in label_counts:
            prob_of_label = label_counts[label] / len(dataset)
            impurity -= prob_of_label**2
        return impurity

    def information_gain(self, starting_labels, split_labels):
        """
        Calculates the information gain after splitting a dataset.

        Args:
            starting_labels (list): The labels before splitting.
            split_labels (list): The labels after splitting.

        Returns:
            float: The information gain after splitting.
        """
        info_gain = self.gini(starting_labels)
        for subset in split_labels:
            info_gain -= self.gini(subset) * len(subset) / len(starting_labels)
        return info_gain

    def print_tree(self, node, spacing="", question_dict=None):
        """
        Prints the decision tree in a readable format.

        Args:
            node (Decision_Node or Leaf): The current node to print.
            spacing (str, optional): The spacing for the current level of the
              tree. Defaults to "".
            question_dict (dict, optional): A dictionary mapping column indices
              to questions. Defaults to a predefined set of questions.
        """
        if question_dict is None:
            question_dict = {
                0: "Buying Price",
                1: "Price of maintenance",
                2: "Number of doors",
                3: "Person Capacity",
                4: "Size of luggage boot",
                5: "Estimated Safety",
            }
        if isinstance(node, self._leaf):
            print(spacing + "Predict", node.predictions)
            return
        print(spacing + question_dict[node.question])
        for _, branch in enumerate(node.branches):
            print(spacing + "--> Branch " + branch.value + ":")
            self.print_tree(branch, spacing + "  ")

    def find_best_split(self, dataset, labels):
        """
        Finds the best feature to split the dataset on.

        Args:
            dataset (list): The dataset to split.
            labels (list): The labels corresponding to the dataset.

        Returns:
            tuple: The best information gain and the best feature index to
              split on.
        """
        best_gain, best_feature = 0, 0
        for feature, _ in enumerate(dataset[0]):
            data_subsets, label_subsets = self.split(dataset, labels, feature)
            gain = self.information_gain(labels, label_subsets)
            if gain > best_gain:
                best_gain, best_feature = gain, feature
        return best_gain, best_feature

    def build_tree(self, rows, labels, value=""):
        """
        Builds the decision tree recursively.

        Args:
            rows (list): The dataset to build the tree on.
            labels (list): The labels corresponding to the dataset.
            value (str, optional): The value of the current node.
                Defaults to "".

        Returns:
            Decision_Node or Leaf: The root of the built decision tree.
        """
        gain, question = self.find_best_split(rows, labels)
        if gain == 0:
            return self._leaf(labels, value)
        data_subsets, label_subsets = self.split(rows, labels, question)
        branches = [
            self.build_tree(data, label, data[0][question])
            for data, label in zip(data_subsets, label_subsets)
        ]
        return self.decision_node(question, branches, value)
