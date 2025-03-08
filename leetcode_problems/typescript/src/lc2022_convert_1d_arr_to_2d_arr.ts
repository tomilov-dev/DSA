function construct2DArray(
  original: number[],
  m: number,
  n: number
): number[][] {
  if (m * n != original.length) {
    return [];
  }
  let res: number[][] = [];
  for (let i = 0; i < m; i++) {
    let sub: number[] = [];
    for (let j = 0; j < n; j++) {
      sub.push(original[i * n + j]);
    }
    res.push(sub);
  }
  return res;
}
