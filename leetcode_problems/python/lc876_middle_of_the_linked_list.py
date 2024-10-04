class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        s = head
        q = head
        while q and q.next:
            q = q.next.next
            s = s.next  # type:ignore

        return s
