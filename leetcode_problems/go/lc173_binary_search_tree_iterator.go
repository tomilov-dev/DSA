package main

type BSTIterator struct {
	stack []int
}

func BSTIteratorInorderDFS(node *TreeNode, stack *[]int) {
	if node == nil {
		return
	}
	BSTIteratorInorderDFS(node.Left, stack)
	*stack = append(*stack, node.Val)
	BSTIteratorInorderDFS(node.Right, stack)
}

func ConstructorBSTIterator(root *TreeNode) BSTIterator {
	it := BSTIterator{}
	BSTIteratorInorderDFS(root, &it.stack)
	i := 0
	j := len(it.stack) - 1
	for i < j {
		it.stack[i], it.stack[j] = it.stack[j], it.stack[i]
		i++
		j--
	}
	return it
}

func (it *BSTIterator) Next() int {
	if len(it.stack) == 0 {
		return -1
	}
	i := len(it.stack) - 1
	v := it.stack[i]
	it.stack = it.stack[:i]
	return v
}

func (it *BSTIterator) HasNext() bool {
	return len(it.stack) > 0
}
