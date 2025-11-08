package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type QuadTree struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *QuadTree
	TopRight    *QuadTree
	BottomLeft  *QuadTree
	BottomRight *QuadTree
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

const MOD = 1_000_000_007
