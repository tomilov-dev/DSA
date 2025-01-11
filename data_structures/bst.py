from abc import ABC, abstractmethod
from typing import Callable
from typing import Any
from typing import Optional
from collections import deque


class AbstractTreeNode:
    key: int
    left: Optional["AbstractTreeNode"]
    right: Optional["AbstractTreeNode"]
    parent: Optional["AbstractTreeNode"]

    empty: bool


class EmptyTreeNode(AbstractTreeNode):
    key = None
    left = None
    right = None
    parent = None

    empty = True


EmptyNode = EmptyTreeNode()


class TreeNode(AbstractTreeNode):
    def __init__(
        self,
        key: int,
        left: AbstractTreeNode | None = None,
        right: AbstractTreeNode | None = None,
        parent: AbstractTreeNode | None = None,
    ):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def empty(self) -> None:
        """Empty means node doesn't have the value"""

        return self.key is None

    @classmethod
    def print(cls, node: "TreeNode") -> None:
        if node.key:
            print(node.key)

    def __repr__(self) -> str:
        return f"node.key={self.key}"


class AbstractBinaryTree(ABC):
    def __init__(self):
        self.root = EmptyNode

    def nodify(self, value: int | TreeNode) -> TreeNode:
        if isinstance(value, TreeNode):
            return value
        return TreeNode(value)

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def min(self):
        pass

    @abstractmethod
    def max(self):
        pass

    @abstractmethod
    def predecessor(self):
        pass

    @abstractmethod
    def successor(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class BinarySearchTree(AbstractBinaryTree):
    def __init__(self) -> None:
        super().__init__()

    def search(
        self,
        key: int,
        node: AbstractTreeNode | None = EmptyNode,
    ) -> TreeNode | None:
        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node is None or node.key == key:
            return node

        if node.key > key:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def insert(self, value: int | AbstractTreeNode) -> None:
        node = self.nodify(value)
        if self.root.empty:
            self.root = node

        else:
            slow = None
            fast = self.root

            while fast != None:
                slow = fast

                if fast.key > node.key:
                    fast = fast.left
                else:
                    fast = fast.right

            node.parent = slow
            if slow.key > node.key:
                slow.left = node
            else:
                slow.right = node

    def min(self, node: AbstractTreeNode | None = EmptyNode) -> TreeNode:
        if isinstance(node, EmptyTreeNode):
            node = self.root

        while node.left != None:
            node = node.left
        return node

    def max(self, node: AbstractTreeNode | None = EmptyNode) -> TreeNode:
        if isinstance(node, EmptyTreeNode):
            node = self.root

        while node.right != None:
            node = node.right
        return node

    def successor(self, node: AbstractTreeNode | None = EmptyNode) -> TreeNode:
        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node.right != None:
            return self.min(node.right)

        parent = node.parent
        while parent != None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def predecessor(self, node: AbstractTreeNode | None = EmptyNode) -> TreeNode:
        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node.left != None:
            return self.max(node.left)

        parent = node.parent
        while parent != None and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    def preorder_traversal(
        self,
        node: AbstractTreeNode | None = EmptyNode,
        hook: Callable[[TreeNode | None], Any] | None = None,
    ) -> None:
        """Default start from the root"""

        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node is None:
            return

        if hook is not None:
            hook(node)

        self.preorder_traversal(node.left, hook)
        self.preorder_traversal(node.right, hook)

    def postorder_traversal(
        self,
        node: AbstractTreeNode | None = EmptyNode,
        hook: Callable[[TreeNode | None], Any] | None = None,
    ) -> None:
        """Default start from the root"""

        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node is None:
            return

        self.postorder_traversal(node.left, hook)
        self.postorder_traversal(node.right, hook)

        if hook is not None:
            hook(node)

    def inorder_traversal(
        self,
        node: AbstractTreeNode | None = EmptyNode,
        hook: Callable[[TreeNode | None], Any] | None = None,
    ) -> None:
        """Default start from the root"""

        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node is None:
            return

        self.inorder_traversal(node.left, hook)

        if hook is not None:
            hook(node)

        self.inorder_traversal(node.right, hook)

    def level_order_traversal(
        self,
        node: AbstractTreeNode | None = EmptyNode,
        hook: Callable[[TreeNode | None], Any] | None = None,
    ) -> None:
        """Default start from the root"""

        if isinstance(node, EmptyTreeNode):
            node = self.root

        if node is None:
            return

        queue = deque([node])
        while queue:
            node = queue.popleft()

            if hook is not None:
                hook(node)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def level_order_traversal_recursive(
        self,
        node_list: list[TreeNode] | None = None,
        hook: Callable[[TreeNode | None], Any] | None = None,
    ) -> None:
        """Default start from the root"""

        if node_list is None:
            node_list = [self.root]

        if len(node_list) == 0:
            return

        childrenList = []
        for node in node_list:
            if hook is not None:
                hook(node)

            if node.left is not None:
                childrenList.append(node.left)
            if node.right is not None:
                childrenList.append(node.right)

        self.level_order_traversal_recursive(childrenList, hook)

    def transplant(
        self,
        rNode: AbstractTreeNode,
        tNode: AbstractTreeNode | None,
    ) -> None:
        """
        1. rNode - replaceable node
        2. tNode - transplantable node
        """

        if rNode.parent == None:
            # case if replaceable node is root
            self.root = tNode
        elif rNode == rNode.parent.left:
            # case if replaceable node is left node
            rNode.parent.left = tNode
        else:
            # case if replaceable node is right node
            rNode.parent.right = tNode

        if tNode is not None:
            # at the end we change tNode parent
            tNode.parent = rNode.parent

    def delete(self, delNode: AbstractTreeNode | None) -> None:
        if delNode is None:
            raise ValueError("The node to be deleted mustn't be NULL")

        if delNode.left is None:
            # 1. case no left child node
            # 2. case no both child nodes - replace the node to NULL
            # because right child is NULL
            self.transplant(delNode, delNode.right)
        elif delNode.right is None:
            # 3. case no right child node
            self.transplant(delNode, delNode.left)
        else:
            # 4. case there are both child nodes
            tNode = self.min(delNode.right)
            if tNode.parent != delNode:
                # 4.2 case if right.left node is not None
                self.transplant(tNode, tNode.right)
                tNode.right = delNode.right
                tNode.right.parent = tNode

            # 4.1 replace the node to founded right.left
            # 4.2 replace the node to transplanted
            self.transplant(delNode, tNode)
            tNode.left = delNode.left
            tNode.left.parent = tNode

    @classmethod
    def from_list(self, array: list[int]) -> "BinarySearchTree":
        bst = BinarySearchTree()
        for value in array:
            bst.insert(value)

        return bst


class NodeCollector:
    def __init__(self):
        self.__container: list[int] = []

    def collect(self, node: AbstractTreeNode) -> None:
        if node and node.key:
            self.__container.append(node.key)

    def values(self) -> list[int]:
        """Just return list of collected values"""
        return self.__container

    def popall(self) -> list[int]:
        """Return a list of collected values and empties the container"""
        values = self.__container
        self.__container = []
        return values


def deletion_correctness(tree: BinarySearchTree, value: int):
    collector = NodeCollector()

    tree.inorder_traversal(hook=collector.collect)
    original = collector.popall()

    tree.delete(tree.search(value))
    tree.inorder_traversal(hook=collector.collect)
    deleted = collector.popall()

    assert value not in deleted
    original.remove(value)
    assert original == deleted


def test():
    collector = NodeCollector()

    values = [10, 7, 25, 5, 6, 15, 30, 20, 13, 27]

    preorder = [10, 7, 5, 6, 25, 15, 13, 20, 30, 27]
    postorder = [6, 5, 7, 13, 20, 15, 27, 30, 25, 10]
    inorder = [5, 6, 7, 10, 13, 15, 20, 25, 27, 30]
    level_order = [10, 7, 25, 5, 15, 30, 6, 13, 20, 27]

    tree = BinarySearchTree.from_list(values)

    tree.preorder_traversal(hook=collector.collect)
    assert preorder == collector.popall()

    tree.postorder_traversal(hook=collector.collect)
    assert postorder == collector.popall()

    tree.inorder_traversal(hook=collector.collect)
    assert inorder == collector.popall()

    tree.level_order_traversal(hook=collector.collect)
    assert level_order == collector.popall()

    tree.level_order_traversal_recursive(hook=collector.collect)
    assert level_order == collector.popall()

    deletion_correctness(tree, 6)
    deletion_correctness(tree, 7)
    deletion_correctness(tree, 15)
    # deletion_correctness(tree, 991)
    deletion_correctness(tree, 10)


if __name__ == "__main__":
    test()
