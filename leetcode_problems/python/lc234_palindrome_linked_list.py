class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class SolutionWithMassive:
    def isPalindrome(self, head: ListNode | None) -> bool:
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next

        p1 = 0
        p2 = len(lst) - 1
        while p1 < p2:
            if lst[p1] != lst[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True


class Solution:
    def middle_node(self, node: ListNode | None) -> ListNode:
        s = head
        q = head
        while q and q.next:
            s = s.next  # type:ignore
            q = q.next.next

        return s  # type:ignore

    def reverse(self, node: ListNode | None) -> ListNode:
        prev = None
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp

        return prev  # type:ignore

    def isPalindrome(self, head: ListNode | None) -> bool:
        middle = self.middle_node(head)
        middle = self.reverse(middle)

        while middle and head:
            if middle.val != head.val:
                return False
            middle = middle.next
            head = head.next

        return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    print(Solution().isPalindrome(head))
