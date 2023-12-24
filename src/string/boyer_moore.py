class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.bad_char = self.bad_character_heuristic(pattern)

    def bad_character_heuristic(self, pattern):
        """
        Preprocesses the pattern to create the bad character heuristic table.
        """
        bad_char = [-1] * 256  # Assuming character set is ASCII
        for i, j in enumerate(pattern):
            bad_char[ord(pattern[i])] = i
        return bad_char

    def search(self, text):
        """
        Search for the pattern in the given text using the Boyer-Moore algorithm.
        """
        m = len(self.pattern)
        n = len(text)
        indexes = []

        s = 0
        while s <= n - m:
            j = m - 1

            while j >= 0 and self.pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                indexes.append(s)
                s += (m - self.bad_char[ord(text[s + m])] if s + m < n else 1)
            else:
                s += max(1, j - self.bad_char[ord(text[s + j])])

        return indexes

# Example usage
pattern = "ABC"
text = "ABABDABACDABABCABAB"
bm = BoyerMoore(pattern)
indexes = bm.search(text)
print(f"Pattern found at indexes: {indexes}")
