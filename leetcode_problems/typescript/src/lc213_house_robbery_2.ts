function robDP(nums: number[]): number {
  if (nums.length == 1) {
    return nums[0];
  }

  let n = nums.length;
  let dp = new Array(n + 1).fill(0);
  dp[1] = nums[0];
  dp[2] = Math.max(nums[1], dp[1]);
  for (let i = 2; i < n; i++) {
    dp[i + 1] = Math.max(dp[i], dp[i - 1] + nums[i]);
  }
  return dp[n];
}

function rob(nums: number[]): number {
  if (nums.length == 1) {
    return nums[0];
  } else if (nums.length == 2) {
    return Math.max(nums[0], nums[1]);
  }

  let nums1 = nums.slice(0, nums.length);
  let nums2 = nums.slice(1, nums.length + 1);
  return Math.max(robDP(nums1), robDP(nums2));
}
