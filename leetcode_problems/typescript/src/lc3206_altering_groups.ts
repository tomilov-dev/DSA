function numberOfAlternatingGroups(colors: number[]): number {
  let n = colors.length;
  let count = 0;
  for (let i = 0; i < n; i++) {
    let j = (i + 1) % n;
    let k = (i + 2) % n;
    if (colors[i] != colors[j] && colors[j] != colors[k]) {
      count++;
    }
  }
  return count;
}
