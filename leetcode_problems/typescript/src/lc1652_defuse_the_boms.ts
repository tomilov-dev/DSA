function decryptIndex(i: number, k: number, n: number): number {
  if (k > 0) {
    return (i + k) % n;
  } else {
    return (i + k + n) % n;
  }
}

function decrypt(code: number[], k: number): number[] {
  let n = code.length;
  let res = new Array(n).fill(0);
  if (k == 0) {
    return res;
  }

  let sum = 0;
  let start = k > 0 ? 1 : k;
  let end = k > 0 ? k : -1;
  for (let i = start; i <= end; i++) {
    sum += code[decryptIndex(0, i, n)];
  }
  for (let i = 0; i < n; i++) {
    res[i] = sum;
    sum -= code[decryptIndex(i, start, n)];
    sum += code[decryptIndex(i, end + 1, n)];
  }
  return res;
}
