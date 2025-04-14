function rob(nums: number[]): number {
  let n: number = nums.length;
  if (n < 2) {
    return nums[0];
  }

  let dp = new Array(n + 1).fill(0);
  dp[1] = nums[0];
  dp[2] = Math.max(nums[1], dp[1]);
  for (let i = 2; i < n; i++) {
    dp[i + 1] = Math.max(dp[i], dp[i - 1] + nums[i]);
  }
  return dp[n];
}
