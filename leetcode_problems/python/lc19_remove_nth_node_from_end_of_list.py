class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def removeNthFromEnd(
        self,
        head: ListNode | None,
        n: int,
    ) -> ListNode | None:
        dummy = ListNode(next=head)
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next  # type: ignore

        slow = dummy
        while fast:
            slow = slow.next  # type:ignore
            fast = fast.next

        slow.next = slow.next.next  # type:ignore
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().removeNthFromEnd(head, 2))
