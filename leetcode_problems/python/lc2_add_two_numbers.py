from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        head = ListNode()
        node = head

        total = carry = 0
        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            node.next = ListNode(num)
            node = node.next

        return head.next


if __name__ == "__main__":
    l1 = build_ll([2, 4, 3])
    l2 = build_ll([5, 6, 4])
    print_ll(Solution().addTwoNumbers(l1, l2))
