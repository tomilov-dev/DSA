from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def swapPairs(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head

        node = dummy
        while node and node.next and node.next.next:
            p1 = node.next
            p2 = node.next.next

            node_next = node.next
            p2_next = p2.next
            node.next = p2
            p2.next = p1
            p1.next = p2_next

            node = node_next

        return dummy.next


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    head = build_ll(arr)
    print_ll(Solution().swapPairs(head))
