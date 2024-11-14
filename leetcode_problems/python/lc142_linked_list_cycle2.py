class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def detectCycle(
        self,
        head: ListNode | None = None,
    ) -> ListNode | None:
        if not head:
            return None

        p1 = head
        p2 = head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break

        if not p1 or not p2 or not p2.next:
            return None

        finder = head
        while finder != p1:
            finder = finder.next
            p1 = p1.next

        return finder


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    cycle = head.next
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next = cycle

    pos = 1
    print(Solution().detectCycle(head))
