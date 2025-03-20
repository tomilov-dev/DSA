class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let dummy = new ListNode();
  let head = dummy;
  while (list1 !== null && list2 !== null) {
    if (list1.val < list2.val) {
      head.next = list1;
      list1 = list1?.next;
    } else {
      head.next = list2;
      list2 = list2?.next;
    }
    head = head.next;
  }
  if (list1 !== null) {
    head.next = list1;
  }
  if (list2 !== null) {
    head.next = list2;
  }
  return dummy.next;
}
