class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
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


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    print(Solution().isPalindrome(head))
