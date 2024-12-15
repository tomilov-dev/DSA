# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head and head.val == val:
            head = head.next

        new_head = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return new_head
