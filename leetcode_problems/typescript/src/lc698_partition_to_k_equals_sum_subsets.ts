function canPartitionKSubsets(nums: number[], k: number): boolean {
  function backtrack(i: number): boolean {
    if (i >= n) {
      for (let sub of subs) {
        if (sub != t) {
          return false;
        }
      }
      return true;
    }

    for (let isub = 0; isub < k; isub++) {
      if (subs[isub] + nums[i] <= t) {
        subs[isub] += nums[i];
        if (backtrack(i + 1)) {
          return true;
        }
        subs[isub] -= nums[i];
      }

      if (subs[isub] == 0) {
        return false;
      }
    }

    return false;
  }

  let n = nums.length;
  let nsum = 0;
  for (let num of nums) {
    nsum += num;
  }

  if (nsum <= 0 || nsum % k != 0) {
    return false;
  }

  let t = Math.floor(nsum / k);
  for (let num of nums) {
    if (num > t) {
      return false;
    }
  }

  nums.sort((a, b) => b - a);
  let subs = new Array(k).fill(0);
  return backtrack(0);
}
