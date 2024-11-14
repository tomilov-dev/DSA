"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution(object):
    """
    53 ms, 20.1 MB
    """

    def hasCycle(self, head: ListNode):
        if not head:
            return False

        try:
            slow = head
            fast = head
            while slow and fast:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False

        except Exception:
            return False


class Solution2:
    def hasCycle(
        self,
        head: ListNode | None = None,
    ) -> bool:
        if not head:
            return False

        p1 = head
        p2 = head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    cycle = head.next
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next = cycle

    pos = 1
    print(Solution().hasCycle(head))
