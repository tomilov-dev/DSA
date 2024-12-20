from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def reverse(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    def getDecimalValue(
        self,
        head: ListNode | None,
    ) -> int:
        head = self.reverse(head)
        res = 0
        mult = 0
        while head:
            res += head.val * (2**mult)
            mult += 1
            head = head.next
        return res


if __name__ == "__main__":
    head = build_ll([1, 0, 1])
    print(Solution().getDecimalValue(head))
