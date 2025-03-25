function isBalancedHeight(
  root: TreeNode | null,
  balanced: { value: boolean }
): number {
  if (root === null) {
    return 0;
  }

  let left = isBalancedHeight(root.left, balanced);
  let right = isBalancedHeight(root.right, balanced);
  if (Math.abs(left - right) > 1) {
    balanced.value = false;
  }
  return Math.max(left, right) + 1;
}

function isBalanced(root: TreeNode | null): boolean {
  let balanced = { value: true };
  isBalancedHeight(root, balanced);
  return balanced.value;
}
