from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def removeZeroSumSublists(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head

        node = dummy
        while node:
            sum = 0
            is_break = False
            forw = node.next
            while forw:
                sum += forw.val
                if sum == 0:
                    node.next = forw.next
                    is_break = True
                    break
                else:
                    forw = forw.next

            if is_break:
                continue
            node = node.next

        return dummy.next


if __name__ == "__main__":
    arr = [1, 2, -3, 3, 1]
    arr = [0, 0]
    head = build_ll(arr)
    print_ll(Solution().removeZeroSumSublists(head))
