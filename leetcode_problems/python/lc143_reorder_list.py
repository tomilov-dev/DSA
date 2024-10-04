# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def premiddle_node(self, node: ListNode | None) -> ListNode:
        s = node
        q = node
        while q and q.next and q.next.next:
            s = s.next  # type:ignore
            q = q.next.next

        return s  # type:ignore

    def reverse(self, node: ListNode | None) -> ListNode:
        prev = None
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp

        return prev  # type:ignore

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        temp = self.premiddle_node(head)
        p2 = self.reverse(temp.next)
        temp.next = None

        new_head = p1 = head
        while p2:
            tmp = p1.next
            p1.next = p2
            p1 = p2
            p2 = tmp


def printit(head: ListNode | None):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    node = Solution().reorderList(head)

    printit(node)
