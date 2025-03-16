function missingNumber(nums: number[]): number {
  let target_sum = 0;
  let current_sum = 0;
  for (let i = 0; i < nums.length + 1; i++) {
    target_sum += i;
  }
  for (let num of nums) {
    current_sum += num;
  }
  return target_sum - current_sum;
}
