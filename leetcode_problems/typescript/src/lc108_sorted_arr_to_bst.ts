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

function inorder_travesal(node: TreeNode | null, hook: CallableFunction): void {
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
): TreeNode | null {
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
  let node = new TreeNode(nums[mid]);

  node.left = sortedArrayToBST(nums, start, mid - 1);
  node.right = sortedArrayToBST(nums, mid + 1, end);

  return node;
}

function printNode(node: TreeNode): void {
  if (node === null) {
    return;
  }
  console.log(node.val);
}

function test() {
  let nums = [-10, -3, 0, 5, 9];
  let root = sortedArrayToBST(nums, 0, nums.length - 1);

  inorder_travesal(root, printNode);
}

test();
