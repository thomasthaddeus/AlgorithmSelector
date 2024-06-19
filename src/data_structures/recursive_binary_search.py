"""data_structures/recursive_binary_search.py

This module implements a recursive version of the binary search algorithm.
Binary search is an efficient algorithm for finding an item from a sorted list
of items. It works by repeatedly dividing in half the portion of the list that
could contain the item, until you've narrowed down the possible locations to
just one.

The recursive implementation involves the function calling itself with updated
bounds based on the comparison between the target and the middle element of the
search range. This module specifically demonstrates how to apply this approach
to locate the position of a target value within a subarray defined by its left
and right bounds.
"""

TARGET = 13


def recursive_binary_search(nums, left, right, target):
    """
    Perform a recursive binary search on a sorted list of numbers.

    Args:
        nums (List[int]): The list of sorted integers to search within.
        left (int): The starting index of the subarray to search within.
        right (int): The ending index of the subarray to search within.
        target (int): The value to search for within the `nums` list.

    Returns:
        int: The index of the `target` in the list `nums` if present;
          otherwise, -1.

    This function splits the search range in half, checking if the target is at
    the middle, or deciding which half of the array to continue searching
    through recursively.
    """
    if left > right:
        return -1  # Base condition: search space is exhausted

    # Calculate mid avoiding overflow
    mid = left + (right - left) // 2

    if target == nums[mid]:
        return mid  # Base condition: target is found
    elif target < nums[mid]:
        return recursive_binary_search(
            nums, left, mid - 1, target
        )  # Search in the left half
    else:
        return recursive_binary_search(
            nums, mid + 1, right, target
        )  # Search in the right half


def search_index():
    """
    Prompts the user to input a list of sorted integers, then searches for a
    pre-defined target using recursive binary search.

    The function reads space-separated integers from input, initializes search
    bounds, and uses `recursive_binary_search` to find the `TARGET` in the
    list. It prints the result of the search.

    Example:
        Input: 2 5 8 10 13 19 21 32 37 52
        Output: Element found at index 4 (if TARGET is 13)
    """
    nums = [
        int(num)
        for num in input("Enter sorted integers separated by space: ").split(" ")
    ]

    (left, right) = (0, len(nums) - 1)
    index = recursive_binary_search(nums, left, right, TARGET)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found in the list")
