from utils import ListNode


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.tail = None
        self.dummy.next = self.tail
        self.len = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1

        head = self.dummy.next
        while index > 0 and head:
            head = head.next
            index -= 1
        return head.val if head else -1

    def addAtHead(self, val: int) -> None:
        head = ListNode(val)
        prev_head = self.dummy.next
        if prev_head:
            head.next = prev_head
        self.dummy.next = head
        if self.len == 0:
            self.tail = head
        self.len += 1

    def addAtTail(self, val: int) -> None:
        tail = ListNode(val)
        if self.tail:
            self.tail.next = tail
            self.tail = self.tail.next
        else:
            self.tail = tail
            self.dummy.next = self.tail
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.len:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.len:
            return self.addAtTail(val)

        to_add = ListNode(val)
        head = self.dummy.next
        while index > 1 and head:
            head = head.next
            index -= 1

        temp = head.next
        head.next = to_add
        head.next.next = temp
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        if index == 0:
            self.dummy.next = self.dummy.next.next
            if self.len == 1:
                self.tail = None
            self.len -= 1
            return

        head = self.dummy.next
        while index > 1 and head:
            head = head.next
            index -= 1

        if head.next == self.tail:
            self.tail = head

        head.next = head.next.next
        self.len -= 1


if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtTail(0)
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)

    ll.addAtIndex(3, 10)

    print(ll.get(5))
