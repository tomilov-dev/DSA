package main

func sortListInsertion(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	dummy := &ListNode{Val: 0, Next: nil}
	right := head
	for right != nil {
		left := dummy
		for left.Next != nil && left.Next.Val < right.Val {
			left = left.Next
		}
		next := right.Next
		right.Next = left.Next
		left.Next = right
		right = next
	}
	return dummy.Next
}

func sortListMerge(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	mid := getMiddle(head)
	right := mid.Next
	mid.Next = nil
	leftSorted := sortListMerge(head)
	rightSorted := sortListMerge(right)
	return merge(leftSorted, rightSorted)
}

func getMiddle(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}

func merge(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			curr.Next = l1
			l1 = l1.Next
		} else {
			curr.Next = l2
			l2 = l2.Next
		}
		curr = curr.Next
	}
	if l1 != nil {
		curr.Next = l1
	}
	if l2 != nil {
		curr.Next = l2
	}
	return dummy.Next
}
