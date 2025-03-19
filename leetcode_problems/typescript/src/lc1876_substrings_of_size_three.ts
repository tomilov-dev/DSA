function countGoodSubstrings(s: string): number {
  let n = s.length;
  let res = 0;
  if (n < 3) {
    return 0;
  }
  for (let i = 0; i < n - 2; i++) {
    if (s[i] !== s[i + 1] && s[i] !== s[i + 2] && s[i + 1] !== s[i + 2]) {
      res++;
    }
  }
  return res;
}
