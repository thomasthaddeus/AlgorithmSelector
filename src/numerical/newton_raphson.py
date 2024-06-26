"""numerical/newton_raphson.py
_summary_

_extended_summary_

Raises:
    ValueError: _description_
    ValueError: _description_

Returns:
    _type_: _description_

Ex:
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

nr = NewtonRaphson(f, df)
root = nr.find_root(initial_guess=1.0)
print("Root found:", root)
"""

class NewtonRaphson:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, function, derivative):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            function (_type_): _description_
            derivative (_type_): _description_
        """
        self.function = function
        self.derivative = derivative

    def find_root(self, initial_guess, tolerance=1e-6, max_iterations=1000):
        """Find the root of the function starting from an initial guess."""
        x0 = initial_guess
        for _ in range(max_iterations):
            f_x0 = self.function(x0)
            f_prime_x0 = self.derivative(x0)
            if f_prime_x0 == 0:
                raise ValueError("Zero derivative. No solution found.")
            x1 = x0 - f_x0 / f_prime_x0
            if abs(x1 - x0) < tolerance:
                return x1
            x0 = x1
        raise ValueError("Exceeded maximum iterations. No solution found.")
