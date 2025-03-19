function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let p1 = 0;
  let p2 = 1;
  let map: Map<number, number> = new Map();
  map.set(nums[p1], 1);
  for (; p2 <= k && p2 < nums.length; p2++) {
    map.set(nums[p2], (map.get(nums[p2]) || 0) + 1);
    if ((map.get(nums[p2]) || 0) > 1) {
      return true;
    }
  }
  for (; p2 < nums.length; p1++, p2++) {
    map.set(nums[p1], (map.get(nums[p1]) || 0) - 1);
    if ((map.get(nums[p2]) || 0) > 0) {
      return true;
    }
    map.set(nums[p2], (map.get(nums[p2]) || 0) + 1);
  }
  return false;
}
