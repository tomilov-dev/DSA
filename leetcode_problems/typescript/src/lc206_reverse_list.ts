function reverseList(head: ListNode | null): ListNode | null {
  let prev = null;
  let cur = head;
  while (cur !== null) {
    let temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp;
  }
  return prev;
}
