import unittest
import LCA

class Node(LCA.Node):
    def __init__(self, value):
        super().__init__(value)

class test_LCA(unittest.TestCase):

    def test_BasicTree(self):
        # print("Test1: Test Basic Tree:")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # visualising the data

        # print(root)

        self.assertEqual(3, LCA.findLCA(root, 6, 7).key, "3 should be the lowest common ancestor of 6 and 7")
        print("Finished test_BasicTree")

    def test_EmptyTree(self):
        # print("Test2: Test Empty Tree:")
        root = None
        self.assertEqual(None, LCA.findLCA(root, 6, 7), " The output should be -1 since the tree is empty")
        print("Finished test_EmptyTree")

    def test_BothNodesNotPresent(self):
        # print("Test3: testBothNodesNotPresent:")
        root = Node(1)
        self.assertEqual(None, LCA.findLCA(root, 6, 7), " The output should be -1 both nodes are missing")
        print("Finished test_BothNodesNotPresent")

    def test_OneNodeNotPresent(self):
        # print("Test4: testOneNodeNotPresent:")
        root = Node(1)
        root.left = Node(6)
        self.assertEqual(None, LCA.findLCA(root, 6, 7).key, " The output should -1 since one of the nodes is missing")

    def test_CommonAncestorIsTarg(self):
        # print("Test5: commonAncestorIsTarget")
        root = Node(1)
        root.left = Node(3)
        root.right = Node(5)
        root.left.left = Node(6)
        root.left.right = Node(8)

        self.assertEqual(1, LCA.findLCA(root, 1, 3).key,
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, LCA.findLCA(root, 1, 5).key,
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(3, LCA.findLCA(root, 3, 6).key,
                         "The output should be 3 since it is both the ancestor node and the target node")
        self.assertEqual(3, LCA.findLCA(root, 3, 8).key,
                         "The output should be 3 since it is both the ancestor node and the target node")

    def test_MissingNode(self):
        # print("Test6: testMissingNode")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(-1, LCA.findLCA(root, 10, 9).key, "Missing node should return -1")

    def test_DuplicateNodesLucky(self):
        # print("Test7: duplicateNodesLucky")
        root = Node(1)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(50)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(1, LCA.findLCA(root, 1, 2).key, "Both the common ancestor and target are separate nodes both" \
                                                           "storing the value 1")

    def test_DuplicateNodes(self):
        # print("Test8: duplicateNodes:")
        root = Node(1)
        root.left = Node(3)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(1, LCA.findLCA(root, 7, 6).key,
                         "There are two instances of the value 6 in the tree, 1 should be returned as it is the common"
                         "ancestor for both values of 6")

        # Example of visualization
        print("Test 8: test_DuplicateNodes")
        print(root)

    def test_Single(self):
        # print("Test9: testSingle")
        root = Node(1)

        assert LCA.findLCA(root, 1, 1).key == 1, \
            "Should be 1 but got: " + str(LCA.findLCA(root, 1, 1))

    def test_CharsInNumberTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)

        self.assertEqual(None, LCA.findLCA(root, 'a', 'b'),
                         "Should be -1 but got: " + str(LCA.findLCA(root, 'a', 'b')))

    def test_CharsInCharTree(self):
        root = Node('a')
        root.left = Node('b')
        root.right = Node('c')
        root.left.left = Node('d')
        root.left.right = Node('e')
        root.right.left = Node('f')
        root.right.right = Node('g')
        root.left.left.left = Node('h')

        self.assertEqual('b', LCA.findLCA(root, 'd', 'e').key,
                         "Should be b but got: " + str(LCA.findLCA(root, 'd', 'e')))

    # Reminder if you don't put the word test in python functions they won't work!!


if __name__ == '__main__':
    unittest.main()