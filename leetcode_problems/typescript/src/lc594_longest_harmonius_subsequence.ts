function findLHS(nums: number[]): number {
  nums.sort((a, b) => a - b);
  let p1 = 0;
  let p2 = 0;
  let max = 0;
  while (p1 < nums.length && p2 < nums.length) {
    if (nums[p2] - nums[p1] == 1) {
      max = Math.max(max, p2 - p1 + 1);
      p2++;
    } else if (nums[p2] - nums[p1] > 1) {
      p1++;
    } else {
      p2++;
    }
  }
  return max;
}
