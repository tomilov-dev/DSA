class TreeNode3 {
  val: number;
  left: TreeNode3 | null;
  right: TreeNode3 | null;
  constructor(val?: number, left?: TreeNode3 | null, right?: TreeNode3 | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function inorderTraversal(
  node: TreeNode3 | null,
  hook: CallableFunction
): void {
  if (node === null) {
    return;
  }

  inorderTraversal(node.left, hook);
  hook(node);
  inorderTraversal(node.right, hook);
}

function balanced_bst(
  nodes: TreeNode3[],
  start: number,
  end: number
): TreeNode3 | null {
  if (start > end) {
    return null;
  }

  let mid = start + Math.floor((end - start) / 2);

  let node = nodes[mid];
  node.left = balanced_bst(nodes, start, mid - 1);
  node.right = balanced_bst(nodes, mid + 1, end);

  return node;
}

function balanceBST(root: TreeNode3 | null): TreeNode3 | null {
  if (root === null) {
    return null;
  }

  let sorted_nodes: TreeNode3[] = [];
  inorderTraversal(root, (node: TreeNode3) => sorted_nodes.push(node));

  root = balanced_bst(sorted_nodes, 0, sorted_nodes.length - 1);
  return root;
}
