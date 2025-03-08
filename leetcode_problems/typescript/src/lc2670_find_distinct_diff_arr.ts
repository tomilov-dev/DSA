function distinctDifferenceArray(nums: number[]): number[] {
  let pd = 0;
  let sd = 0;
  let diff: number[] = [];
  let pm = new Map<number, number>();
  let sm = new Map<number, number>();

  for (let num of nums) {
    if ((pm.get(num) || 0) == 0) {
      pd++;
    }
    pm.set(num, (pm.get(num) || 0) + 1);
  }

  for (let num of nums) {
    pm.set(num, (pm.get(num) || 0) - 1);
    if ((sm.get(num) || 0) == 0) {
      sd++;
    }
    sm.set(num, (sm.get(num) || 0) + 1);
    if ((pm.get(num) || 0) == 0) {
      pd--;
    }
    diff.push(sd - pd);
  }

  return diff;
}

console.log(distinctDifferenceArray([1, 2, 3, 4, 5]));
