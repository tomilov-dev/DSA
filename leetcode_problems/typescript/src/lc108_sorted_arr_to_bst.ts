class TreeNode1 {
  val: number;
  left: TreeNode1 | null;
  right: TreeNode1 | null;
  constructor(val?: number, left?: TreeNode1 | null, right?: TreeNode1 | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function inorder_travesal(
  node: TreeNode1 | null,
  hook: CallableFunction
): void {
  if (node === null) {
    return;
  }

  inorder_travesal(node.left, hook);
  hook(node);
  inorder_travesal(node.right, hook);
}

function sortedArrayToBST(
  nums: number[],
  start: number | null = null,
  end: number | null = null
): TreeNode1 | null {
  if (start === null) {
    start = 0;
  }
  if (end === null) {
    end = nums.length - 1;
  }
  if (start > end) {
    return null;
  }

  let mid = start + Math.floor((end - start) / 2);
  let node = new TreeNode1(nums[mid]);

  node.left = sortedArrayToBST(nums, start, mid - 1);
  node.right = sortedArrayToBST(nums, mid + 1, end);

  return node;
}

function printNode(node: TreeNode1): void {
  if (node === null) {
    return;
  }
  console.log(node.val);
}
