function maxUniqueSplit(s: string): number {
  function backtrack(i: number): number {
    if (i >= n) {
      return uniq.size;
    }

    let max = 0;
    for (let j = i + 1; j < n + 1; j++) {
      let sub = s.slice(i, j);
      if (!uniq.has(sub)) {
        uniq.add(sub);
        let maxi = backtrack(j);
        max = Math.max(max, maxi);
        uniq.delete(sub);
      }
    }
    return max;
  }

  const n = s.length;
  let uniq = new Set<string>();
  return backtrack(0);
}
