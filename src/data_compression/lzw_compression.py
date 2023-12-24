class LZWCompression:
    def __init__(self):
        self.dictionary_size = 256
        self.dictionary = {chr(i): i for i in range(self.dictionary_size)}

    def compress(self, input_string):
        """
        Compress a string using LZW algorithm.

        Args:
            input_string (str): The string to compress.

        Returns:
            list: A list of codes representing the compressed string.
        """
        w = ""
        compressed_data = []
        for c in input_string:
            wc = w + c
            if wc in self.dictionary:
                w = wc
            else:
                compressed_data.append(self.dictionary[w])
                # Add wc to the dictionary.
                self.dictionary[wc] = self.dictionary_size
                self.dictionary_size += 1
                w = c
        if w:
            compressed_data.append(self.dictionary[w])
        return compressed_data

    def decompress(self, compressed_data):
        """
        Decompress a list of output ks to a string.

        Args:
            compressed_data (list): The compressed data.

        Returns:
            str: The decompressed string.
        """
        reversed_dictionary = {i: chr(i) for i in range(self.dictionary_size)}
        w = chr(compressed_data.pop(0))
        decompressed_data = w
        for k in compressed_data:
            if k in reversed_dictionary:
                entry = reversed_dictionary[k]
            elif k == self.dictionary_size:
                entry = w + w[0]
            decompressed_data += entry

            # Add w+entry[0] to the dictionary.
            reversed_dictionary[self.dictionary_size] = w + entry[0]
            self.dictionary_size += 1

            w = entry
        return decompressed_data

# Example usage
lzw = LZWCompression()

# Compress
compressed = lzw.compress("TOBEORNOTTOBEORTOBEORNOT")
print("Compressed:", compressed)

# Decompress
decompressed = lzw.decompress(compressed)
print("Decompressed:", decompressed)
