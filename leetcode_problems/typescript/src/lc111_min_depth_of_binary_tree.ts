function minDepthRec(node: TreeNode | null): number {
  if (node === null) {
    return 10 ** 7;
  }
  if (node.left === null && node.right === null) {
    return 1;
  }
  let left = minDepthRec(node.left);
  let right = minDepthRec(node.right);
  return Math.min(left, right) + 1;
}

function minDepth(root: TreeNode | null): number {
  if (root === null) {
    return 0;
  }
  return minDepthRec(root);
}
