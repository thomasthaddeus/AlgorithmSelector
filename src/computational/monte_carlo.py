"""computational/monte_carlo.py

This module contains a general Monte Carlo simulation framework and a specific example of estimating π. The example provided demonstrates how to estimate π using this framework.

The Monte Carlo method is a computational algorithm that relies on repeated random sampling to obtain numerical results. It's particularly useful for estimating unknown quantities when deterministic solutions are infeasible or difficult to compute.

Monte Carlo simulations are often used when:
1. Complex Systems: The system is too complex for analytical or exact solutions.
2. Probabilistic Problems: The problem involves probability and randomness,
   making stochastic modeling appropriate.
3. Large-Scale Problems: The problem has a large number of variables or
   possible outcomes, where exhaustive computation is impractical.

Monte Carlo methods are advantageous over deterministic alternatives because:
1. Simplicity: They can be simpler to implement and understand for certain
   problems.
2. Flexibility: They can adapt to different types of problems, including those
   with random behavior or uncertain parameters.
3. Scalability: They scale well with increased computational power, allowing
   for more accurate approximations with larger samples.

Returns:
    Monte Carlo framework objects for different estimation purposes.
"""

import random
from typing import Tuple

class MonteCarlo:
    """
    A general Monte Carlo simulation framework.
    """
    def __init__(self, iterations: int):
        """
        Initializes the Monte Carlo simulation.

        Args:
            iterations: The number of iterations to run the simulation.
        """
        self.iterations = iterations

    def sample(self) -> Tuple[float, float]:
        """
        Generates a random sample.

        This function should be overridden to generate samples
        specific to the problem being solved.

        Returns:
            tuple: A sample represented as a tuple.
        """
        return random.random(), random.random()

    def evaluate(self, sample: Tuple[float, float]) -> bool:
        """
        Evaluates a sample.

        This function should be overridden to evaluate whether
        the sample meets the desired criteria.

        Args:
            sample: The sample to evaluate.

        Returns:
            bool: True if the sample meets the criteria, False otherwise.
        """
        x, y = sample
        return x * x + y * y <= 1

    def run(self) -> float:
        """
        Runs the Monte Carlo simulation.

        Returns:
            The proportion of samples that passed the evaluation function.
        """
        successful = 0

        for _ in range(self.iterations):
            sample = self.sample()
            if self.evaluate(sample):
                successful += 1

        return successful / self.iterations

class MonteCarloPiEstimator(MonteCarlo):
    """
    A specialized Monte Carlo estimator for π.
    """
    def sample(self) -> Tuple[float, float]:
        """
        Generates a random point within a unit square.

        Returns:
            tuple: A point represented as a tuple (x, y).
        """
        return random.random(), random.random()

    def evaluate(self, sample: Tuple[float, float]) -> bool:
        """
        Evaluates if a point is inside a unit circle.

        Args:
            sample: A point represented as a tuple (x, y).

        Returns:
            bool: True if the point is inside the unit circle, False otherwise.
        """
        x, y = sample
        return x * x + y * y <= 1

def estimator_example():
    """
    An example of using the Monte Carlo method to estimate π.
    """
    estimator = MonteCarloPiEstimator(iterations=100000)
    estimated_pi = estimator.run() * 4
    print(f"Estimated value of π: {estimated_pi}")
