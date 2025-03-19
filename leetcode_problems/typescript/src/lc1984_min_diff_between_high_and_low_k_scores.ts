function minimumDifference(nums: number[], k: number): number {
  let n = nums.length;
  nums.sort((a, b) => a - b);
  let max = 10000001;
  for (let i = 0; i <= n - k; i++) {
    max = Math.min(max, nums[i + k - 1] - nums[i]);
  }
  return max;
}
