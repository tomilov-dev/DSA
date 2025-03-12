function shortestToChar(s: string, c: string): number[] {
  let n = s.length;
  let res = new Array(n).fill(Number.MAX_SAFE_INTEGER);
  let prev = -1;
  for (let i = 0; i < n; i++) {
    if (s[i] == c) {
      prev = i;
    }
    if (prev > -1) {
      res[i] = i - prev;
    }
  }
  prev = -1;
  for (let i = n - 1; i >= 0; i--) {
    if (s[i] == c) {
      prev = i;
    }
    if (prev > -1) {
      res[i] = Math.min(prev - i, res[i]);
    }
  }
  return res;
}
