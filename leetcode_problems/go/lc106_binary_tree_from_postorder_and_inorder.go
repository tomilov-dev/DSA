package main

func buildTreePostorderInorderHelper(postorder []int, postStart, postEnd int, inorder []int, inStart, inEnd int, inMap map[int]int) *TreeNode {
	if postStart < postEnd || inStart > inEnd {
		return nil
	}

	rootVal := postorder[postStart]
	root := &TreeNode{Val: rootVal}
	inRoot := inMap[rootVal]
	rightSize := inEnd - inRoot

	root.Right = buildTreePostorderInorderHelper(postorder, postStart-1, postStart-rightSize, inorder, inRoot+1, inEnd, inMap)
	root.Left = buildTreePostorderInorderHelper(postorder, postStart-rightSize-1, postEnd, inorder, inStart, inRoot-1, inMap)
	return root
}

func buildTreePostorderInorder(inorder []int, postorder []int) *TreeNode {
	inMap := make(map[int]int)
	for i, v := range inorder {
		inMap[v] = i
	}
	return buildTreePostorderInorderHelper(postorder, len(postorder)-1, 0, inorder, 0, len(inorder)-1, inMap)
}
