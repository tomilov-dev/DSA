function minimumRecolors(blocks: string, k: number): number {
  let n = blocks.length;
  let w = 0;
  let min = 0;
  for (let i = 0; i < k && i < n; i++) {
    if (blocks[i] === "W") {
      w++;
    }
  }
  min = w;
  for (let i = k; i < n; i++) {
    if (blocks[i - k] === "W") {
      w--;
    }
    if (blocks[i] === "W") {
      w++;
    }
    min = Math.min(min, w);
  }
  return min;
}
