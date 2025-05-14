from typing import Union


class TreeNode:
    def __init__(
        self,
        value: int,
        left: Union["TreeNode", None] = None,
        right: Union["TreeNode", None] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def bottomView(self, root: TreeNode | None) -> list[int]:
        def rec(node: TreeNode | None, hor: int, vert: int) -> None:
            if not node:
                return None

            if hor not in map or vert >= map[hor][1]:
                map[hor] = (node.value, vert)

            rec(node.left, hor - 1, vert + 1)
            rec(node.right, hor + 1, vert + 1)

        map = {}
        result = []
        rec(root, 0, 0)
        for hor in sorted(map.keys()):
            result.append(map[hor][0])
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(6)

    print(Solution().bottomView(root))
