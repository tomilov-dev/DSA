function hasPathSumRec(
  node: TreeNode | null,
  sum: number,
  targetSum: number
): boolean {
  if (node === null) {
    return false;
  }
  sum += node.val;
  if (sum === targetSum && node.left === null && node.right === null) {
    return true;
  }
  return (
    hasPathSumRec(node.left, sum, targetSum) ||
    hasPathSumRec(node.right, sum, targetSum)
  );
}

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (root === null) {
    return false;
  }
  return hasPathSumRec(root, 0, targetSum);
}
