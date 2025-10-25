package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
