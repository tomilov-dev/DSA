function arraySign(nums: number[]): number {
  let m = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      return 0;
    } else if (nums[i] < 0) {
      m++;
    }
  }
  if (m % 2 == 0) {
    return 1;
  } else {
    return -1;
  }
}
