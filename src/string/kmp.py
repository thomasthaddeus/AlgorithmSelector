class KMP:
    def __init__(self, word):
        self.word = word
        self.lps = self.compute_lps_array(word)

    def compute_lps_array(self, word):
        """
        Computes the Longest Prefix Suffix (LPS) array used in KMP algorithm.
        """
        lps = [0] * len(word)
        length = 0
        i = 1

        while i < len(word):
            if word[i] == word[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, text):
        """
        Search the word in the given text string and return the index of first occurrence.
        """
        M, N = len(self.word), len(text)
        i = j = 0

        while i < N:
            if self.word[j] == text[i]:
                i += 1
                j += 1

            if j == M:
                return i - j  # Found a match

            elif i < N and self.word[j] != text[i]:
                if j != 0:
                    j = self.lps[j - 1]
                else:
                    i += 1

        return -1  # No match found

# Example usage
word = "ABABCABAB"
text = "ABABDABACDABABCABAB"
kmp = KMP(word)
index = kmp.search(text)
print(f"Pattern found at index: {index}")
