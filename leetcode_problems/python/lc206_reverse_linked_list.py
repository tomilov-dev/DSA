class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def reverseList(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        prev = None
        node = head
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp

        return prev


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().reverseList(head))
