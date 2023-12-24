import unittest
from data_structures.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_insertion(self):
        avl_tree = AVLTree()
        avl_tree.insert(3)
        avl_tree.insert(2)
        avl_tree.insert(1)
        self.assertEqual(avl_tree.root.key, 2)

if __name__ == '__main__':
    unittest.main()
