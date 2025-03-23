function preorderTraversalRecursion(node: TreeNode | null, res: number[]) {
  if (node === null) {
    return;
  }

  res.push(node.val);
  preorderTraversalRecursion(node.left, res);
  preorderTraversalRecursion(node.right, res);
}

function preorderTraversal(root: TreeNode | null): number[] {
  let res: number[] = [];
  preorderTraversalRecursion(root, res);
  return res;
}
