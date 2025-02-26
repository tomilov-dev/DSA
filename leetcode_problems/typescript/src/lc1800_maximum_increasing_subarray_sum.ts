function maxAscendingSum(nums: number[]): number {
  let maxsum = nums[0];
  let cursum = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > nums[i - 1]) {
      cursum += nums[i];
    } else {
      maxsum = Math.max(maxsum, cursum);
      cursum = nums[i];
    }
    if (i == nums.length - 1) {
      maxsum = Math.max(maxsum, cursum);
    }
  }
  return maxsum;
}

console.log(maxAscendingSum([10, 20, 30, 5, 10, 50]));
