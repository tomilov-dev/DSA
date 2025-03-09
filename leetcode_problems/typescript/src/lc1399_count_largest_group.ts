function digit_sum(n: number): number {
  let sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }
  return sum;
}

function countLargestGroup(n: number): number {
  let arr: number[] = new Array(50).fill(0);
  let maxv: number = 0;
  for (let i = 1; i <= n; i++) {
    let ds = digit_sum(i);
    arr[ds]++;
    maxv = Math.max(maxv, arr[ds]);
  }
  let res = 0;
  for (let i = 0; i < 50; i++) {
    if (arr[i] === maxv) {
      res++;
    }
  }
  return res;
}
