package main

func robRecursiveHelper(node *TreeNode) int {
	if node == nil {
		return 0
	}
	take := node.Val
	if node.Left != nil {
		take += robRecursiveHelper(node.Left.Left) + robRecursiveHelper(node.Left.Right)
	}
	if node.Right != nil {
		take += robRecursiveHelper(node.Right.Left) + robRecursiveHelper(node.Right.Right)
	}
	not_take := robRecursiveHelper(node.Left) + robRecursiveHelper(node.Right)
	return max(take, not_take)
}

func robRecursive(root *TreeNode) int {
	return robRecursiveHelper(root)
}

func robTopDownHelper(node *TreeNode, mem map[*TreeNode]int) int {
	if node == nil {
		return 0
	}
	key := node
	if _, solved := mem[key]; !solved {
		take := node.Val
		if node.Left != nil {
			take += robTopDownHelper(node.Left.Left, mem) + robTopDownHelper(node.Left.Right, mem)
		}
		if node.Right != nil {
			take += robTopDownHelper(node.Right.Left, mem) + robTopDownHelper(node.Right.Right, mem)
		}
		not_take := robTopDownHelper(node.Left, mem) + robTopDownHelper(node.Right, mem)
		mem[key] = max(take, not_take)
	}
	return mem[key]
}

func robTopDown(root *TreeNode) int {
	mem := make(map[*TreeNode]int, 0)
	return robTopDownHelper(root, mem)
}
