from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def partition(
        self,
        head: ListNode | None,
        x: int,
    ) -> ListNode | None:
        if not head:
            return head

        dummy1 = ListNode()
        small = dummy1

        dummy2 = ListNode()
        large = dummy2

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = dummy2.next

        return dummy1.next


if __name__ == "__main__":
    arr = [1, 4, 3, 2, 5, 2]
    head = build_ll(arr)
    x = 3
    print_ll(Solution().partition(head, x))
