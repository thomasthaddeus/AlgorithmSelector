"""numerical/euclidean.py
_summary_

_extended_summary_

Returns:
    _type_: _description_

# Example usage
euclidean = EuclideanAlgorithm()
gcd_result = euclidean.gcd(48, 18)
print(f"The GCD of 48 and 18 is {gcd_result}.")
"""

class EuclideanAlgorithm:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        pass

    def gcd(self, a, b):
        """Compute the greatest common divisor of a and b."""
        while b != 0:
            a, b = b, a % b
        return a
