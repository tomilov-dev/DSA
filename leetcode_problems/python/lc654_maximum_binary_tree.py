from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def find_max_index(
        self,
        nums: list[int],
        start: int,
        end: int,
    ) -> int:
        max_v = float("-inf")
        max_i = None

        for index in range(start, end + 1):
            if nums[index] > max_v:
                max_v = nums[index]
                max_i = index

        return max_i

    def construct(
        self,
        nums: list[int],
        start: int,
        end: int,
    ) -> Optional[TreeNode]:
        if start > end:
            return None

        max_i = self.find_max_index(nums, start, end)

        node = TreeNode(val=nums[max_i])
        left = self.construct(nums, start, max_i - 1)
        right = self.construct(nums, max_i + 1, end)

        node.left = left
        node.right = right
        return node

    def constructMaximumBinaryTree(
        self,
        nums: List[int],
    ) -> Optional[TreeNode]:
        return self.construct(nums, 0, len(nums) - 1)


def inorder_traversal(node: TreeNode):
    if node is None:
        return

    inorder_traversal(node.left)
    print(node)
    inorder_traversal(node.right)


if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]

    sol = Solution()
    root = sol.constructMaximumBinaryTree(nums)

    if root:
        inorder_traversal(root)
