"""binary_search_tree.py
Binary Search Tree operations in Python

This script implements the operations of a Binary Search Tree (BST) in Python.
It includes the following operations:
- Creating a node
- Inorder traversal
- Inserting a node
- Finding the inorder successor
- Deleting a node

"""

class Node:
    """Class representing a node in a binary search tree."""

    def __init__(self, key):
        """Initialize a new node with the given key.

        Args:
            key: The value of the node.
        """
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    """Perform inorder traversal of the binary search tree.

    Args:
        root: The root node of the binary search tree.

    Returns:
        None
    """
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=" ")
        inorder(root.right)


def insert(node, key):
    """Insert a node with the given key into the binary search tree.

    Args:
        node: The root node of the binary search tree.
        key: The value to be inserted.

    Returns:
        The updated root node of the binary search tree.
    """
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    """Find the node with the minimum value in the binary search tree.

    Args:
        node: The root node of the binary search tree.

    Returns:
        The node with the minimum value.
    """
    current = node

    while current.left is not None:
        current = current.left

    return current


def delete_node(root, key):
    """Delete a node with the given key from the binary search tree.

    Args:
        root: The root node of the binary search tree.
        key: The value to be deleted.

    Returns:
        The updated root node of the binary search tree.
    """
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    return root


if __name__ == "__main__":
    root = None
    root = insert(root, 2)
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 10)
    root = insert(root, 13)
    root = insert(root, 19)
    root = insert(root, 21)
    root = insert(root, 32)
    root = insert(root, 37)
    root = insert(root, 52)

    print("Inorder traversal:", end=" ")
    inorder(root)

    print("\nDelete 10")
    root = delete_node(root, 10)
    print("Inorder traversal:", end=" ")
    inorder(root)
