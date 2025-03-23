function postorderTraversalRecursion(node: TreeNode | null, res: number[]) {
  if (node === null) {
    return;
  }

  postorderTraversalRecursion(node.left, res);
  postorderTraversalRecursion(node.right, res);
  res.push(node.val);
}

function postorderTraversal(root: TreeNode | null): number[] {
  let res: number[] = [];
  postorderTraversalRecursion(root, res);
  return res;
}
