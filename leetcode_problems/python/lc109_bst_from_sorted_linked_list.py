class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def balanced_tree(
        self,
        nums: list[int],
        start: int,
        end: int,
    ) -> TreeNode:
        if start > end:
            return None

        mid = end + (start - end) // 2

        node = TreeNode(nums[mid])
        node.left = self.balanced_tree(nums, start, mid - 1)
        node.right = self.balanced_tree(nums, mid + 1, end)

        return node

    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        array = []
        while head:
            array.append(head.val)
            head = head.next

        return self.balanced_tree(array, 0, len(array) - 1)


if __name__ == "__main__":
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)

    sol = Solution()
    bst = sol.sortedListToBST(head)

    print(bst)
