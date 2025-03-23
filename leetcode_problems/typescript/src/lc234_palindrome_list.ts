function getMiddleNode(head: ListNode): ListNode {
  let slow = head;
  let fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}

function reverseMiddleNode(head: ListNode): ListNode {
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

function isPalindrome(head: ListNode | null): boolean {
  let middle = getMiddleNode(head);
  middle = reverseMiddleNode(middle);
  while (middle !== null && head !== null) {
    if (middle.val != head.val) {
      return false;
    }
    middle = middle.next;
    head = head.next;
  }
  return true;
}
