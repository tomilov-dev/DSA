from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def reverseBetween(
        self,
        head: ListNode | None,
        left: int,
        right: int,
    ) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode()
        dummy.next = head

        start = None
        node = dummy
        for _ in range(left):
            if node:
                start = node
                node = node.next
        start.next = None

        reverse = None
        end = None
        while node:
            if left - 1 == right:
                end = node
                break

            temp = node.next
            node.next = reverse
            reverse = node
            node = temp
            left += 1

        start.next = reverse
        while reverse and reverse.next:
            reverse = reverse.next
        reverse.next = end

        return dummy.next


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = build_ll(arr)
    left = 2
    right = 4
    print_ll(Solution().reverseBetween(head, left, right))
