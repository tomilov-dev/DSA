import sys
import pytest
import random
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from bst import BinarySearchTree, NodeCollector


class BaseBSTTest:
    @pytest.fixture
    def bst_cls(self) -> BinarySearchTree:
        return BinarySearchTree

    @pytest.fixture
    def test_values(self):
        return [10, 7, 25, 5, 6, 15, 30, 20, 13, 27]

    @pytest.fixture
    def preorder(self):
        return [10, 7, 5, 6, 25, 15, 13, 20, 30, 27]

    @pytest.fixture
    def postorder(self):
        return [6, 5, 7, 13, 20, 15, 27, 30, 25, 10]

    @pytest.fixture
    def inorder(self):
        return [5, 6, 7, 10, 13, 15, 20, 25, 27, 30]

    @pytest.fixture
    def level_order(self):
        return [10, 7, 25, 5, 15, 30, 6, 13, 20, 27]

    @pytest.fixture
    def filled_tree(self, test_values) -> BinarySearchTree:
        return BinarySearchTree.from_list(test_values)

    def deletion_correctness(
        self,
        tree: BinarySearchTree,
        value: int,
    ):
        collector = NodeCollector()

        tree.inorder_traversal(hook=collector.collect)
        original = collector.popall()

        tree.delete(tree.search(value))
        tree.inorder_traversal(hook=collector.collect)
        deleted = collector.popall()

        assert value not in deleted
        original.remove(value)
        assert original == deleted

    def test_insert(self, bst_cls, test_values: list[int]):
        bst: BinarySearchTree = bst_cls()

        bst.insert(test_values[0])
        assert bst.root.key == test_values[0]

        bst.insert(test_values[1])
        assert bst.root.left.key == test_values[1]

        bst.insert(test_values[2])
        assert bst.root.right.key == test_values[2]

    def test_inorder_traversal(
        self,
        filled_tree: BinarySearchTree,
        inorder: list[int],
    ):
        collector = NodeCollector()
        filled_tree.inorder_traversal(hook=collector.collect)

        assert collector.popall() == inorder

    def test_preorder_traversal(
        self,
        filled_tree: BinarySearchTree,
        preorder: list[int],
    ):
        collector = NodeCollector()
        filled_tree.preorder_traversal(hook=collector.collect)

        assert collector.popall() == preorder

    def test_postorder_traversal(
        self,
        filled_tree: BinarySearchTree,
        postorder: list[int],
    ):
        collector = NodeCollector()
        filled_tree.postorder_traversal(hook=collector.collect)

        assert collector.popall() == postorder

    def test_level_order_traversal(
        self,
        filled_tree: BinarySearchTree,
        level_order: list[int],
    ):
        collector = NodeCollector()
        filled_tree.level_order_traversal(hook=collector.collect)

        assert collector.popall() == level_order

    def test_min(
        self,
        filled_tree: BinarySearchTree,
        test_values: list[int],
    ):
        min_node = filled_tree.min()
        assert min_node.key == min(test_values)

    def test_max(
        self,
        filled_tree: BinarySearchTree,
        test_values: list[int],
    ):
        max_node = filled_tree.max()
        assert max_node.key == max(test_values)

    def test_search(
        self,
        filled_tree: BinarySearchTree,
        test_values: list[int],
    ):
        root = filled_tree.search(test_values[0])
        assert root.key == filled_tree.root.key == test_values[0]

        node = filled_tree.search(test_values[-1])
        assert node.key == test_values[-1]

        number = filled_tree.max().key + 1
        null_node = filled_tree.search(number)
        assert null_node is None

    def test_successor(
        self,
        filled_tree: BinarySearchTree,
        inorder: list[int],
    ):
        k = len(inorder) // 2
        node = None
        while k < len(inorder):
            value = inorder[k]
            if node is None:
                node = filled_tree.search(value)
                assert node.key == value
            else:
                node = filled_tree.successor(node)
                assert node.key == value
            k += 1

    def test_predecessor(
        self,
        filled_tree: BinarySearchTree,
        inorder: list[int],
    ):
        k = len(inorder) // 2
        node = None
        while k > 0:
            value = inorder[k]
            if node is None:
                node = filled_tree.search(value)
                assert node.key == value
            else:
                node = filled_tree.predecessor(node)
                assert node.key == value
            k -= 1

    def test_transplant(
        self,
        filled_tree: BinarySearchTree,
        test_values: list[int],
    ):
        test_values = sorted(test_values)

        kf = 2
        tNode = None
        while tNode is None:
            to_replace = test_values[len(test_values) // kf]

            rNode = filled_tree.search(to_replace)
            if rNode.left is not None:
                tNode = rNode.left
            elif rNode.right is not None:
                tNode = rNode.right
            else:
                kf *= 0.8
                continue

        rParent = rNode.parent

        filled_tree.transplant(rNode, tNode)
        isleft = rParent.left.key == tNode.key
        isright = rParent.right.key == tNode.key

        assert isleft or isright  # we do not check not AND
        assert rParent.key == tNode.parent.key

    def test_deletion(
        self,
        filled_tree: BinarySearchTree,
    ):
        self.deletion_correctness(filled_tree, 6)
        self.deletion_correctness(filled_tree, 7)
        self.deletion_correctness(filled_tree, 15)
        self.deletion_correctness(filled_tree, 10)

        collector = NodeCollector()
        filled_tree.inorder_traversal(hook=collector.collect)
        inorder = collector.popall()

        del_value = inorder[len(inorder) // 2]
        self.deletion_correctness(filled_tree, del_value)


class TestBinarySearchTree(BaseBSTTest):
    pass
