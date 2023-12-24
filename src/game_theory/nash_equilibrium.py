import numpy as np
import nashpy as nash

class NashEquilibriumSolver:
    def __init__(self, player1_payoffs, player2_payoffs):
        self.game = nash.Game(player1_payoffs, player2_payoffs)

    def find_nash_equilibrium(self):
        """
        Find the Nash Equilibrium of the game.

        Returns:
            list: A list of Nash Equilibria.
        """
        return list(self.game.support_enumeration())

# Example usage
player1_payoffs = np.array([[3, 1], [0, 2]])
player2_payoffs = np.array([[2, 1], [0, 3]])

solver = NashEquilibriumSolver(player1_payoffs, player2_payoffs)
nash_equilibria = solver.find_nash_equilibrium()

print("Nash Equilibria:")
for eq in nash_equilibria:
    print(eq)
