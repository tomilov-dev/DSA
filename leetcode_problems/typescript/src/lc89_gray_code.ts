function grayCode(n: number): number[] {
  function grayCodeBackTrack(n: number) {
    if (res.length === 1 << n) {
      return true;
    }

    let last = res[res.length - 1];
    for (let i = 0; i < n; i++) {
      let next = last ^ (1 << i);
      if (!visited.has(next)) {
        res.push(next);
        visited.add(next);
        if (grayCodeBackTrack(n)) {
          return true;
        }
        res.pop();
        visited.delete(next);
      }
    }
    return false;
  }

  let visited = new Set<number>([0]);
  let res: number[] = [0];
  grayCodeBackTrack(n);
  return res;
}
