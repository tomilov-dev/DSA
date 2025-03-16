function searchIsGood(value: number, target: number): boolean {
  return value <= target;
}

function search(nums: number[], target: number): number {
  let low = 0;
  let high = nums.length;
  while (high - low > 1) {
    let mid = low + Math.floor((high - low) / 2);
    if (searchIsGood(nums[mid], target)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return nums[low] == target ? low : -1;
}
