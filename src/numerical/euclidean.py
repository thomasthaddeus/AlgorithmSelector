class EuclideanAlgorithm:
    def __init__(self):
        pass

    def gcd(self, a, b):
        """Compute the greatest common divisor of a and b."""
        while b != 0:
            a, b = b, a % b
        return a

# Example usage
euclidean = EuclideanAlgorithm()
gcd_result = euclidean.gcd(48, 18)
print(f"The GCD of 48 and 18 is {gcd_result}.")
