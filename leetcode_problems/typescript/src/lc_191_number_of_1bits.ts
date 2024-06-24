function hammingWeight(n: number): number {
  let cur_n = n;
  let count = 0;

  while (cur_n > 0) {
    let degree = 0;

    while (2 ** degree <= cur_n) {
      degree += 1;
    }

    cur_n -= 2 ** Math.max(degree - 1, 0);
    count += 1;
  }
  return count;
}
