class RabinKarp:
    def __init__(self, pattern, base=256):
        self.pattern = pattern
        self.pattern_length = len(pattern)
        self.base = base  # The base value for the rolling hash function
        self.pattern_hash = self.hash_function(pattern)
        self.large_prime = 101  # A large prime number for modulo operation

    def hash_function(self, string):
        """Computes the hash value of a string."""
        h = 0
        for character in string:
            h = (h * self.base + ord(character)) % self.large_prime
        return h

    def search(self, text):
        """Searches for the pattern in the given text and returns the index of the first occurrence."""
        n = len(text)
        text_hash = self.hash_function(text[:self.pattern_length])

        for i in range(n - self.pattern_length + 1):
            if text_hash == self.pattern_hash and text[i:i+self.pattern_length] == self.pattern:
                return i  # Match found

            if i < n - self.pattern_length:
                # Calculate hash value for next window of text: Remove leading character, add trailing character
                text_hash = (text_hash - ord(text[i]) * pow(self.base, self.pattern_length - 1, self.large_prime)) % self.large_prime
                text_hash = (text_hash * self.base + ord(text[i + self.pattern_length])) % self.large_prime
                text_hash = (text_hash + self.large_prime) % self.large_prime

        return -1  # No match found

# Example usage
pattern = "abc"
text = "hello abc world abc good"
rk = RabinKarp(pattern)
index = rk.search(text)
print(f"Pattern found at index: {index}")
