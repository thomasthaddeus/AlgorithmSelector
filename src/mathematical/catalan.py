"""
catalan.py

This implementation of the Catalan numbers demonstrates how to efficiently
calculate the nth Catalan number. More info at: <https://en.wikipedia.org/wiki/
Catalan_number>
"""

def catalan(num) -> int:
    """
    Returns the nth Catalan number which gives the number of unique binary
    search trees which has exactly n nodes of unique values between 1 and n.
    Let us denote it by Cn:
        number of unique binary search trees

        C0 = 1 and Cn+1 = 2(2n+1)Cn/(n+2)

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if num < 0 or not isinstance(num, int):
        raise ValueError("Input must be a non-negative integer.")

    num_c = 1
    for i in range(0, num):
        num_c: float = num_c * 2 * (2 * i + 1) / (i + 2)
    return int(num_c)


print(f"C1 = {catalan(1)}")  # C1 = 1
print(f"C3 = {catalan(3)}")  # C3 = 5
