import random
from math import gcd

class ShorsAlgorithm:
    def __init__(self, N):
        self.N = N  # The number to factorize

    def find_period(self, a):
        """
        Find the period using a quantum computer (simulated here).
        In actual implementation, this step would use Quantum Fourier Transform.
        """
        # Quantum computation simulation: returns a random period
        return random.randint(1, self.N - 1)

    def factorize(self):
        if self.N % 2 == 0:
            return 2, self.N // 2

        while True:
            a = random.randint(2, self.N - 1)
            if gcd(a, self.N) != 1:
                continue

            r = self.find_period(a)

            if r % 2 != 0 or pow(a, r // 2, self.N) == -1:
                continue

            factor1 = gcd(pow(a, r // 2) - 1, self.N)
            factor2 = gcd(pow(a, r // 2) + 1, self.N)
            return factor1, factor2

# Example usage
N = 15  # Example number to factorize
shor = ShorsAlgorithm(N)
factors = shor.factorize()
print(f"The factors of {N} are {factors}")
