function isGood(nums: number[]): boolean {
  let map: Map<number, number> = new Map();
  let maxv = Number.MIN_SAFE_INTEGER;
  let minv = Number.MAX_SAFE_INTEGER;
  for (let num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
    maxv = Math.max(maxv, num);
    minv = Math.min(minv, num);
  }
  if (minv !== 1 || (map.get(maxv) || 0) !== 2) {
    return false;
  }
  for (let index = 1; index < maxv; index++) {
    if ((map.get(index) || 0) != 1) {
      return false;
    }
  }
  return true;
}
