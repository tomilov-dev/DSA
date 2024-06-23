function sol1(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
}

function sol2(nums: number[], target: number): number[] {
  let hash = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    hash.set(nums[i], i);
  }

  for (let i = 0; i < nums.length; i++) {
    let spread = target - nums[i];
    let j = hash.get(spread);
    if (j !== undefined) {
      if (i !== j) {
        return [i, j];
      }
    }
  }
  return [];
}

let nums = [2, 11, 15, 7];
let target = 9;
console.log(sol2(nums, target));
