from typing import Any, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


def build_ll(arr: list[Any]) -> Optional[ListNode]:
    if not arr:
        return None

    head = ListNode(arr[0])
    node = head
    for el in arr[1:]:
        node.next = ListNode(el)
        node = node.next
    return head


def print_ll(node: Optional[ListNode]) -> None:
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


def insert_tree_level_order(
    arr: list[Any], root: Optional[TreeNode], i: int, n: int
) -> Optional[TreeNode]:
    if i < n:
        if arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp

            root.left = insert_tree_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_tree_level_order(arr, root.right, 2 * i + 2, n)
        else:
            root = None
    return root


def build_tree(arr: list[Any]) -> Optional[TreeNode]:
    return insert_tree_level_order(arr, None, 0, len(arr))


def print_tree(root: Optional[TreeNode]) -> None:
    def height(root: Optional[TreeNode]) -> int:
        return 1 + max(height(root.left), height(root.right)) if root else -1

    nlevels = height(root)
    width = pow(2, nlevels + 1)

    q = [(root, 0, width, "c")]
    levels = []

    while q:
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])

            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.left, level + 1, x - seg, "l"))
            q.append((node.right, level + 1, x + seg, "r"))

    for i, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ""
        pstr = ""
        seg = width // (pow(2, i + 1))
        for n in l:
            valstr = str(n[0].val)
            if n[3] == "r":
                linestr += (
                    " " * (n[2] - preline - 1 - seg - seg // 2)
                    + "¯" * (seg + seg // 2)
                    + "\\"
                )
                preline = n[2]
            if n[3] == "l":
                linestr += " " * (n[2] - preline - 1) + "/" + "¯" * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += " " * (n[2] - pre - len(valstr)) + valstr
            pre = n[2]
        print(linestr)
        print(pstr)


if __name__ == "__main__":
    nums = [1, 2, 3, None, 5]
    tree = build_tree(nums)
    print_tree(tree)
    ll = build_ll([1, 2, 3, 4, 5])
    print_ll(ll)
