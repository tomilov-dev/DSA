from utils import ListNode
from utils import build_ll
from utils import print_ll


class Solution:
    def len(self, head: ListNode | None):
        if not head:
            return 0

        len = 0
        while head:
            head = head.next
            len += 1

        return len

    def rotateRight(
        self,
        head: ListNode | None,
        k: int,
    ) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head

        len = self.len(head)
        if len == 0:
            return dummy.next

        k %= len
        shift = len - k
        if shift == 0:
            return dummy.next

        end_pointer = head
        start_pointer = None
        node = head
        for _ in range(shift - 1):
            node = node.next

        start_pointer = node.next
        dummy.next = start_pointer
        node.next = None

        node = start_pointer
        while node and node.next:
            node = node.next

        if node:
            node.next = end_pointer
        else:
            dummy.next = end_pointer

        return dummy.next


class SolutionEfficient:
    def rotateRight(
        self,
        head: ListNode | None,
        k: int,
    ) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = build_ll(arr)
    k = 2

    arr = [0, 1, 2]
    head = build_ll(arr)
    k = 4

    arr = [1]
    head = build_ll(arr)
    k = 0

    print(Solution().rotateRight(head, k))
