function numTilePossibilities(tiles: string): number {
  function backtrack() {
    for (let i = 0; i < 26; i++) {
      if (arr[i] <= 0) {
        continue;
      }
      arr[i]--;
      count++;
      backtrack();
      arr[i]++;
    }
  }

  let count = 0;
  let arr = new Array(26).fill(0);
  for (let chr of tiles) {
    arr[chr.charCodeAt(0) - "a".charCodeAt(0)]++;
  }
  backtrack();
  return count;
}
