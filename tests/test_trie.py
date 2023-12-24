import unittest
from data_structures.trie import Trie

class TestTrie(unittest.TestCase):
    def test_trie_operations(self):
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("world"))
        self.assertTrue(trie.starts_with("he"))

if __name__ == '__main__':
    unittest.main()