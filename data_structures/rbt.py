from abc import ABC, abstractmethod
from enum import Enum

from bst import AbstractBinaryTree


class NodeColor(Enum):
    RED = "RED"
    BLACK = "BLACK"


class AbstractRBTreeNode:
    key: int
    left: "AbstractRBTreeNode"
    right: "AbstractRBTreeNode"
    parent: "AbstractRBTreeNode"
    color: NodeColor

    empty: bool


class RBTreeNode(AbstractRBTreeNode):
    def __init__(
        self,
        key: int,
        color: NodeColor,
        left: AbstractRBTreeNode | None = None,
        right: AbstractRBTreeNode | None = None,
        parent: AbstractRBTreeNode | None = None,
    ):
        self.key = key
        self.color = color

        self.left = left
        self.right = right
        self.parent = parent

    @property
    def empty(self) -> None:
        """Empty means node doesn't have the value"""

        return self.key is None

    @classmethod
    def print(cls, node: "RBTreeNode") -> None:
        if node.key:
            print(node.key)

    def __repr__(self) -> str:
        return f"node.key={self.key}"


class RBTree(AbstractBinaryTree):
    def __init__(self):
        self.NULL = RBTreeNode(None, None, None, None, None)

        self.root = self.NULL

    def left_rotate(self, x: AbstractRBTreeNode) -> None:
        y: AbstractRBTreeNode = x.right
        if y is self.NULL:
            raise ValueError("Left Child Node shouldn't be NULL")

        x.right = y.left
        if y.left is not self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is self.NULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y: AbstractRBTreeNode) -> None:
        x = y.left
        if x is self.NULL:
            raise ValueError("Right Child Node shouldn't be NULL")

        y.left = x.right
        if x.right is not self.NULL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is self.NULL:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert(self, node: AbstractRBTreeNode) -> None:
        slow = None
        fast = self.root

        while fast is not self.NULL:
            slow = fast
            if node.key < fast.key:
                fast = fast.left
            else:
                fast = fast.right

        node.parent = slow
        if slow.parent is self.NULL:
            self.root = node
        elif node.key < slow.key:
            slow.left = node
        else:
            slow.right = node

        node.left = self.NULL
        node.right = self.NULL
        node.color = NodeColor.RED

        self.insert_fixup(node)

    def insert_fixup(self, node: AbstractRBTreeNode) -> None:
        while node.parent.color == NodeColor.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == NodeColor.RED:
                    node.parent.color = NodeColor.BLACK
                    y.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    self.right_rotate(node.parent.parent)

            else:
                y = node.parent.parent.left
                if y.color == NodeColor.RED:
                    node.parent.color = NodeColor.BLACK
                    y.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    self.right_rotate(node.parent.parent)

    def search(self):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def predecessor(self):
        pass

    def successor(self):
        pass

    def delete(self):
        pass
