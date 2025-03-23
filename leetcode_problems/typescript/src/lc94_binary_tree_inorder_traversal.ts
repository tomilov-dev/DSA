class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function inorderTraversalRecursion(node: TreeNode | null, res: number[]) {
  if (node === null) {
    return;
  }

  inorderTraversalRecursion(node.left, res);
  res.push(node.val);
  inorderTraversalRecursion(node.right, res);
}

function inorderTraversal(root: TreeNode | null): number[] {
  let res: number[] = [];
  inorderTraversalRecursion(root, res);
  return res;
}
