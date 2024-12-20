from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def deleteDuplicates(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head

        p1 = dummy
        p2 = head
        while p1 and p2:
            if p2.next and p2.val == p2.next.val:
                while p2 and p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                p2 = p2.next
                p1.next = p2

            else:
                p1 = p2
                p2 = p2.next

        return dummy.next


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 4, 4, 5]
    head = build_ll(arr)
    print_ll(Solution().deleteDuplicates(head))
