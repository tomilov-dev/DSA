package main

import "math"

func isValidBSTHelper(node *TreeNode, mini int, maxi int) bool {
	if node == nil {
		return true
	}
	if node.Val <= mini || node.Val >= maxi {
		return false
	}
	return isValidBSTHelper(node.Left, mini, node.Val) && isValidBSTHelper(node.Right, node.Val, maxi)
}

func isValidBST(root *TreeNode) bool {
	return isValidBSTHelper(root, math.MinInt64, math.MaxInt64)
}
