package main

func buildTreeHelper(preorder []int, preStart, preEnd int, inorder []int, inStart, inEnd int, inMap map[int]int) *TreeNode {
	if preStart > preEnd || inStart > inEnd {
		return nil
	}
	rootVal := preorder[preStart]
	root := &TreeNode{Val: rootVal}
	inRoot := inMap[rootVal]
	leftSize := inRoot - inStart

	root.Left = buildTreeHelper(preorder, preStart+1, preStart+leftSize, inorder, inStart, inRoot-1, inMap)
	root.Right = buildTreeHelper(preorder, preStart+leftSize+1, preEnd, inorder, inRoot+1, inEnd, inMap)
	return root
}

func buildTreeDivideAndConquer(preorder []int, inorder []int) *TreeNode {
	inMap := make(map[int]int)
	for i, v := range inorder {
		inMap[v] = i
	}
	return buildTreeHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
}
