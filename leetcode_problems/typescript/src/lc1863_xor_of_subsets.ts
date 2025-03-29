function subsetXORSum(nums: number[]): number {
  function backtrack(i: number) {
    sum += xor;
    for (let j = i; j < nums.length; j++) {
      xor ^= nums[j];
      backtrack(j + 1);
      xor ^= nums[j];
    }
  }

  let sum = 0;
  let xor = 0;
  backtrack(0);
  return sum;
}
