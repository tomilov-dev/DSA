class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def nextLargerNodes(
        self,
        head: ListNode | None,
    ) -> list[int]:
        if not head:
            return []

        values = []
        while head:
            values.append(head.val)
            head = head.next

        stack = []
        result = [0] * len(values)

        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                result[stack.pop()] = value
            stack.append(i)

        return result


if __name__ == "__main__":
    head = ListNode(2)
    head.next = ListNode(7)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)

    print(Solution().nextLargerNodes(head))
