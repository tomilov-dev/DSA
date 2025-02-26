class TreeNode2 {
  val: number;
  left: TreeNode2 | null;
  right: TreeNode2 | null;

  constructor(val?: number, left?: TreeNode2 | null, right?: TreeNode2 | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function findMaxIndex(nums: number[], start: number, end: number): number {
  let max_v = Number.NEGATIVE_INFINITY;
  let max_i = -1;

  for (let index = start; index <= end; index++) {
    if (nums[index] > max_v) {
      max_v = nums[index];
      max_i = index;
    }
  }

  return max_i;
}

function construct(
  nums: number[],
  start: number,
  end: number
): TreeNode2 | null {
  if (start > end) {
    return null;
  }

  let max_i = findMaxIndex(nums, start, end);
  let node = new TreeNode2(nums[max_i]);

  node.left = construct(nums, start, max_i - 1);
  node.right = construct(nums, max_i + 1, end);

  return node;
}

function constructMaximumBinaryTree(nums: number[]): TreeNode2 | null {
  return construct(nums, 0, nums.length - 1);
}
