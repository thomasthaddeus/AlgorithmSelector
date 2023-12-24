import random

class MonteCarloPiEstimator:
    def __init__(self, iterations):
        self.iterations = iterations

    def estimate_pi(self):
        inside_circle = 0

        for _ in range(self.iterations):
            x, y = random.random(), random.random()
            if x*x + y*y <= 1:  # Check if the point is inside the quarter circle
                inside_circle += 1

        return (inside_circle / self.iterations) * 4  # Pi is approximately 4 times the ratio

# Example usage
estimator = MonteCarloPiEstimator(iterations=100000)
estimated_pi = estimator.estimate_pi()
print(f"Estimated value of π: {estimated_pi}")
