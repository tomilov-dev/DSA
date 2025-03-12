function findContentChildren(g: number[], s: number[]): number {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);
  let p1 = 0;
  let p2 = 0;
  let res = 0;
  while (p1 < g.length && p2 < s.length) {
    if (g[p1] <= s[p2]) {
      p1++;
      p2++;
      res++;
    } else {
      p2++;
    }
  }
  return res;
}
