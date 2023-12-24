"""sieve_of_eratosthenes.py

_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import os
import logging
import time

class PrimeSieve:
    """
     _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    LOG_DIR = "logs"
    LOG_FILE = f"{LOG_DIR}/prime_calculations.log"

    def __init__(self):
        self.setup_logging()

    def setup_logging(self):
        """
        Set up logging configuration.
        """
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        logging.basicConfig(
            filename=self.LOG_FILE,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        console = logging.StreamHandler()
        console.setLevel(logging.WARNING)
        logging.getLogger("").addHandler(console)

    def logrotate(self, max_size=5, backup_count=3):
        """
        Rotate the log file if it exceeds the specified size.

        Args:
            max_size (int, optional): Maximum size of the log file in MB. Defaults to 5MB.
            backup_count (int, optional): Number of backup files to keep. Defaults to 3.
        """
        logfile = self.LOG_FILE
        if not os.path.exists(logfile):
            return

        file_size = os.path.getsize(logfile) / (1024 * 1024)  # Convert size to MB

        if file_size < max_size:
            return

        for i in range(backup_count - 1, 0, -1):
            src = f"{logfile}.{i}"
            dst = f"{logfile}.{i+1}"
            if os.path.exists(src):
                os.rename(src, dst)

        os.rename(logfile, f"{logfile}.1")

    def sieve_of_eratosthenes(self, n):
        """
        Calculate prime numbers up to a given number using the Sieve of Eratosthenes.

        Args:
            n (int): The upper limit up to which prime numbers are to be calculated.

        Returns:
            list[int]: A list of prime numbers up to the given number n.
        """
        start_time = time.time()

        if n < 2:
            return []

        prime = [True] * (n + 1)
        prime[0], prime[1] = False, False

        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                if (p > 2 and p % 2 == 0) or (p > 5 and p % 10 == 5) or self.sum_of_digits(p) in [3, 6, 9]:
                    prime[p] = False
                    continue
                for i in range(p**2, n + 1, p):
                    prime[i] = False

        primes = [i for i, is_prime in enumerate(prime) if is_prime]

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        self.log(elapsed_time, len(primes))
        return primes

    @staticmethod
    def sum_of_digits(num):
        """
        Calculate the sum of digits of a given number.

        Args:
            num (int): The number whose digits are to be summed.

        Returns:
            int: The sum of the digits of the given number.
        """
        return sum(int(digit) for digit in str(num))

    @staticmethod
    def log(elapsed_time, num_primes):
        """
        Log the calculation time and the total number of primes calculated.
        Also performs log rotation.

        Args:
            elapsed_time (float): The time taken for the prime number calculation in milliseconds.
            num_primes (int): The total number of prime numbers calculated.
        """
        logging.info("Calculation time: %.2f milliseconds", elapsed_time)
        logging.info("Total number of primes calculated: %d", num_primes)
        logging.warning("Checkpoint: Calculated primes up to %d. Check the log file for details.", num_primes)

    @staticmethod
    def total_of_primes(primes):
        """
        Calculate the total sum of a list of prime numbers.

        Args:
            primes (list[int]): A list of prime numbers.

        Returns:
            int: The total sum of the given list of prime numbers.
        """
        return sum(primes)

# Example usage
sieve = PrimeSieve()
n = 10000
p = sieve.sieve_of_eratosthenes(n)
sieve.logrotate()
print(f"Total of all primes up to {n}: {PrimeSieve.total_of_primes(p)}")
