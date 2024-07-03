import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def find(
        self,
        node: ListNode,
        pos: int,
    ) -> ListNode:
        count = 0
        while node and count < pos:
            count += 1
            node = node.next
        return node

    def partition(
        self,
        head: ListNode,
        start: int,
        end: int,
    ) -> int:
        x = self.find(head, end)

        i = start
        j = start

        inode = self.find(head, start)
        jnode = inode

        while j < end:
            if jnode.val <= x.val:
                inode.val, jnode.val = jnode.val, inode.val
                inode = inode.next
                i += 1

            jnode = jnode.next
            j += 1

        inode.val, jnode.val = jnode.val, inode.val
        return i

    def random_partition(
        self,
        head: ListNode,
        start: int,
        end: int,
    ) -> int:
        i = random.randint(start, end)
        n1 = self.find(head, end)
        n2 = self.find(head, i)
        n1.val, n2.val = n2.val, n1.val
        return self.partition(head, start, end)

    def quick_sort(
        self,
        head: ListNode,
        start: int,
        end: int,
    ):
        if start >= end:
            return

        q = self.random_partition(head, start, end)
        self.quick_sort(head, start, q - 1)
        self.quick_sort(head, q + 1, end)

    def list_length(self, head: ListNode) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def sortList(self, head: ListNode | None) -> ListNode | None:
        length = self.list_length(head)
        self.quick_sort(head, 0, length - 1)
        return head


def lprint(node: ListNode):
    array = []
    while node:
        array.append(node.val)
        node = node.next
    print(array)


if __name__ == "__main__":
    head = ListNode(-1)
    head.next = ListNode(5)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)

    lprint(head)

    sol = Solution()
    res = sol.sortList(head)

    lprint(res)
