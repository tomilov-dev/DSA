from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def oddEvenList(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        odd = ListNode()
        odd_start = odd
        even = ListNode()
        even_start = even

        index = 0
        node = head
        while node:
            if index % 2 == 0:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next

            node = node.next
            index += 1

        even.next = None
        odd.next = None

        head = odd_start.next
        odd.next = even_start.next

        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = build_ll(arr)
    print_ll(Solution().oddEvenList(head))
