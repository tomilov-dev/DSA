function countArrangement(n: number): number {
  function backtrack(cur: number) {
    if (cur > n) {
      count += 1;
      return;
    }

    for (let i = 0; i < n; i++) {
      if (arr[i] !== 0) {
        continue;
      }
      if (cur % (i + 1) !== 0 && (i + 1) % cur !== 0) {
        continue;
      }

      arr[i] = cur;
      backtrack(cur + 1);
      arr[i] = 0;
    }
  }

  let count = 0;
  let arr: number[] = new Array(n).fill(0);
  backtrack(1);
  return count;
}
