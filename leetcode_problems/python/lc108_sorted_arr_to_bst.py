"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""

from typing import Union, Callable


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Union["TreeNode", None] = None,
        right: Union["TreeNode", None] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


def preorder_traversal(
    node: TreeNode,
    hook: Callable[[TreeNode | None], None],
) -> None:
    if node is None:
        return

    hook(node)
    preorder_traversal(node.left, hook)
    preorder_traversal(node.right, hook)


def inorder_traversal(
    node: TreeNode,
    hook: Callable[[TreeNode | None], None],
) -> None:
    if node is None:
        return

    inorder_traversal(node.left, hook)
    hook(node)
    inorder_traversal(node.right, hook)


def print_node(node: TreeNode) -> None:
    if node is None:
        return
    print(node.val)


def balanced_tree(
    nums: list[int],
    start: int,
    end: int,
) -> TreeNode:
    if start > end:
        return None

    mid = end + (start - end) // 2

    node = TreeNode(nums[mid])
    node.left = balanced_tree(nums, start, mid - 1)
    node.right = balanced_tree(nums, mid + 1, end)

    return node


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]

    root = balanced_tree(nums, 0, len(nums) - 1)

    inorder_traversal(root, print_node)
