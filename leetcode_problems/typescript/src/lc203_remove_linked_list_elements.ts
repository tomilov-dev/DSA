function removeElements(head: ListNode | null, val: number): ListNode | null {
  let dummy = ListNode(0, head);
  let node = dummy;
  while (node.next !== null) {
    if (node.next.val === val) {
      node.next = node.next.next;
    } else {
      node = node.next;
    }
  }
  return dummy.next;
}
