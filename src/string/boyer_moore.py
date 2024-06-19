"""string/boyer_moore.py
This module implements the Boyer-Moore string search algorithm.

The Boyer-Moore algorithm is an efficient string searching algorithm that skips
portions of the text to improve search time. It uses two heuristics to
determine how far to skip: the bad character heuristic and the good suffix
heuristic. In this implementation, only the bad character heuristic is used,
which generally provides good performance when the pattern length is smaller
compared to the text.

The algorithm is useful when you need to search for a pattern in a large text
efficiently. It is particularly useful when the text is very large and the
pattern occurs infrequently.

# Example usage
PATTERN = "ABC"
TEXT = "ABABDABACDABABCABAB"
bm = BoyerMoore(PATTERN)
indexes = bm.search(TEXT)
print(f"Pattern found at indexes: {indexes}")
"""

class BoyerMoore:
    """
    A class to represent the Boyer-Moore string search algorithm.

    This class uses the bad character heuristic to efficiently search
    for a pattern in a given text.
    """
    def __init__(self, pattern):
        """
        Initializes the Boyer-Moore search with a given pattern.

        Args:
            pattern: The pattern to search for.
        """
        self.pattern = pattern
        self.bad_char = self.bad_character_heuristic(pattern)

    def bad_character_heuristic(self, pattern):
        """
        Preprocesses the pattern to create the bad character heuristic table.

        The bad character heuristic table records the last occurrence of each
        character in the pattern, which helps in determining how far to shift
        the pattern when a mismatch occurs.

        Args:
            pattern: The pattern to preprocess.

        Returns:
            list: The bad character heuristic table.
        """
        bad_char = [-1] * 256  # Assuming character set is ASCII
        for i, char in enumerate(pattern):
            bad_char[ord(char)] = i
        return bad_char

    def search(self, text):
        """
        Search for the pattern in the given text using the Boyer-Moore algorithm.

        The search method uses the preprocessed bad character heuristic table to
        find all occurrences of the pattern in the text.

        Args:
            text: The text to search in.

        Returns:
            list: A list of starting indexes where the pattern is found.
        """
        m = len(self.pattern)
        n = len(text)
        idxs = []

        s = 0
        while s <= n - m:
            j = m - 1

            while j >= 0 and self.pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                idxs.append(s)
                s += (m - self.bad_char[ord(text[s + m])] if s + m < n else 1)
            else:
                s += max(1, j - self.bad_char[ord(text[s + j])])

        return idxs
