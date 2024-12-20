from utils import ListNode
from utils import build_ll
from utils import print_ll


class SolutionWrong:
    def deleteNode(self, head: ListNode) -> None:
        p1 = head
        p2 = head.next
        while p1 and p2 and p2.next:
            p1.val = p2.val
            p2 = p2.next
            p1 = p1.next

        p1.val = p2.val
        p1.next = None


class Solution:
    def deleteNode(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return

        head.val = head.next.val
        head.next = head.next.next


if __name__ == "__main__":
    arr = [4, 5, 1, 9]
    origin = build_ll(arr)
    head = origin.next
    Solution().deleteNode(head)

    print_ll(origin)
