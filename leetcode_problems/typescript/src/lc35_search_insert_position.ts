function _searchInsertIsGood(value: number, target: number): boolean {
  return value < target;
}

function searchInsert(nums: number[], target: number): number {
  let low = -1;
  let high = nums.length;
  while (high - low > 1) {
    let mid = low + Math.floor((high - low) / 2);
    if (_searchInsertIsGood(nums[mid], target)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return high;
}
