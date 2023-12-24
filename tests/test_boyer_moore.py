import unittest
from string.boyer_moore import BoyerMoore

class TestBoyerMoore(unittest.TestCase):
    def test_boyer_moore_search(self):
        bm = BoyerMoore("example")
        self.assertEqual(bm.search("This is an example"), 11)
        self.assertEqual(bm.search("No matches"), -1)

if __name__ == '__main__':
    unittest.main()
