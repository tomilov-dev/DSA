function findMaxAverage(nums: number[], k: number): number {
  let sum = 0;
  let max = 0;
  for (let i = 0; i < k && i < nums.length; i++) {
    sum += nums[i];
  }
  max = sum / k;
  for (let i = k; i < nums.length; i++) {
    sum -= nums[i - k];
    sum += nums[i];
    max = Math.max(max, sum / k);
  }
  return max;
}
