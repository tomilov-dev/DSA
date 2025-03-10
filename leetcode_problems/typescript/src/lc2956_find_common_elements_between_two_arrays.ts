function findIntersectionValues(nums1: number[], nums2: number[]): number[] {
  let m1: Map<number, number> = new Map();
  let m2: Map<number, number> = new Map();
  for (let num of nums1) {
    m1.set(num, (m1.get(num) || 0) + 1);
  }
  for (let num of nums2) {
    m2.set(num, (m2.get(num) || 0) + 1);
  }

  let r1 = 0;
  let r2 = 0;
  m1.forEach((v, k) => {
    if ((m2.get(k) || 0) > 0) {
      r1 += v;
    }
  });
  m2.forEach((v, k) => {
    if ((m1.get(k) || 0) > 0) {
      r2 += v;
    }
  });

  return [r1, r2];
}
