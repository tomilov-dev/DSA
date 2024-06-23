"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def run(
        self,
        head1: ListNode,
        head2: ListNode,
    ) -> ListNode:
        newHead = ListNode()
        current = newHead

        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        if head1 or head2:
            current.next = head1 if head1 else head2

        return newHead.next


def printer(head: ListNode):
    node = head
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    head1 = ListNode(2)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(0)
    head2.next = ListNode(1)
    head2.next.next = ListNode(5)

    sol = Solution()
    head = sol.run(head1, head2)

    printer(head)
