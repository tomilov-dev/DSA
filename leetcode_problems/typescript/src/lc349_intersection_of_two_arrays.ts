function intersection(nums1: number[], nums2: number[]): number[] {
  nums1.sort((a, b) => a - b);
  nums2.sort((a, b) => a - b);
  let p1 = 0;
  let p2 = 0;
  let res: number[] = [];
  while (p1 < nums1.length && p2 < nums2.length) {
    if (nums1[p1] < nums2[p2]) {
      p1++;
    } else if (nums1[p1] > nums2[p2]) {
      p2++;
    } else {
      if (res.length == 0 || res[res.length - 1] != nums1[p1]) {
        res.push(nums1[p1]);
      }
      p1++;
      p2++;
    }
  }
  return res;
}
